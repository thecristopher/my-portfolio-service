from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from random import randint

from data import (
    projects_data,
    skills_data,
    navbar_data,
    about_me_data,
    contact_info_data,
)

from models import Project, Skill, NavBarItem, AboutMe, ContactInfo, RollResult


app = FastAPI(
    title="My Portfolio API",
    description="API that feeds data to cristophercervantes.com",
    version="1.0.0",
)

origins = [
    "http://localhost:5173",  # Local development
    "https://cristophercervantes.com",  # Production URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.get("/roll", response_model=RollResult)
def perception_check():
    roll = randint(1, 20)
    success = roll >= 10
    message = "Success!" if success else "Failure! You rolled a low number, try again."
    return RollResult(roll=roll, success=success, message=message)
