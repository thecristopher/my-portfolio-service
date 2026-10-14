import os
import time
from random import randint

from fastapi import FastAPI, HTTPException, Response, Request, Cookie
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from data import (
    projects_data,
    skills_data,
    navbar_data,
    about_me_data,
    contact_info_data,
)

import github
from models import Project, Skill, NavBarItem, AboutMe, ContactInfo, RollResult, GitHubRepo


# Railway sets these on every deploy, so the interactive docs only show up locally
IS_PRODUCTION = any(name in os.environ for name in ("RAILWAY_ENVIRONMENT_ID", "RAILWAY_ENVIRONMENT"))

app = FastAPI(
    title="My Portfolio API",
    description="API that feeds data to cristophercervantes.com",
    version="1.0.0",
    docs_url=None if IS_PRODUCTION else "/docs",
    redoc_url=None if IS_PRODUCTION else "/redoc",
    openapi_url=None if IS_PRODUCTION else "/openapi.json",
)

origins = [
    "http://localhost:5173",  # Local development
    "https://cristophercervantes.com",  # Production URL
    "https://www.cristophercervantes.com",
]

# the site only ever reads from the API and never sends cookies across origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET"],
)

SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "no-referrer",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    # nothing here is a page, so a response should never load or run anything
    "Content-Security-Policy": "default-src 'none'; frame-ancestors 'none'",
    "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
}

RATE_LIMIT_REQUESTS = 60
RATE_LIMIT_WINDOW_SECONDS = 60
_hits = {}


def client_ip(request):
    # Railway's proxy appends the real address last, anything before it came from the client and can be forged
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[-1].strip()
    return request.client.host if request.client else "unknown"


def is_rate_limited(ip, now):
    window_start, count = _hits.get(ip, (now, 0))
    if now - window_start >= RATE_LIMIT_WINDOW_SECONDS:
        window_start, count = now, 0
    _hits[ip] = (window_start, count + 1)
    # forget visitors whose window ran out so the table can't grow forever
    if len(_hits) > 10_000:
        for stale_ip in [key for key, (start, _) in _hits.items() if now - start >= RATE_LIMIT_WINDOW_SECONDS]:
            del _hits[stale_ip]
    return count + 1 > RATE_LIMIT_REQUESTS


@app.middleware("http")
async def harden_responses(request: Request, call_next):
    if is_rate_limited(client_ip(request), time.monotonic()):
        response = JSONResponse(
            {"detail": "Too many requests, take a breather."},
            status_code=429,
            headers={"Retry-After": str(RATE_LIMIT_WINDOW_SECONDS)},
        )
    else:
        response = await call_next(request)
    for header, value in SECURITY_HEADERS.items():
        # the local docs pages pull Swagger and ReDoc from a CDN, which this policy would block
        if header == "Content-Security-Policy" and request.url.path in ("/docs", "/redoc"):
            continue
        response.headers.setdefault(header, value)
    return response


@app.get("/")
def read_root():
    return {"message": "Portfolio API is alive!"}


@app.get("/navbar", response_model=list[NavBarItem])
def get_navbar():
    """
    Retrieve the navigation bar items.
    """
    return navbar_data


@app.get("/about", response_model=AboutMe)
def get_about():
    """
    Retrieve the about me section.
    """
    return about_me_data


@app.get("/contact", response_model=ContactInfo)
def get_contact():
    """
    Retrieve the contact information.
    """
    return contact_info_data


@app.get("/projects", response_model=list[Project])
def get_projects():
    """
    Retrieve the list of projects.
    """
    return projects_data


@app.get("/skills", response_model=list[Skill])
def get_skills():
    """
    Retrieve the list of skills.
    """
    return skills_data


@app.get("/github/repos", response_model=list[GitHubRepo])
def get_github_repos():
    """
    Retrieve my personal GitHub repos, each pitched by its README.
    """
    try:
        return github.get_repos()
    except OSError:
        raise HTTPException(status_code=502, detail="GitHub isn't answering right now.")


@app.get("/roll", response_model=RollResult)
def perception_check(
    response: Response,
    request: Request,
    failed_before: bool = Cookie(default=False, alias="failed_once")
):
    roll = randint(1, 20)
    success = roll >= 8

    if success:
        message = "Check passed. Nice roll."
        response.delete_cookie("failed_once", httponly=True, secure=True, samesite="lax")
    else:
        if failed_before:
            message = "Failed again. The dice are not on your side."
        else:
            message = "Check failed. Roll again?"
            # remember the miss so a second failure gets a different line
            response.set_cookie(
                key="failed_once",
                value="true",
                max_age=60 * 60,
                httponly=True,
                secure=True,
                samesite="lax",
            )

    return RollResult(roll=roll, success=success, message=message)
