# my-portfolio-service

The FastAPI backend that feeds [cristophercervantes.com](https://cristophercervantes.com). It serves the bio, work history, skills, navigation and contact info as JSON, my GitHub repos pitched by their READMEs, plus a d20 roll for a little game on the site.

The frontend lives in [my-portfolio](https://github.com/thecristopher/my-portfolio).

## Endpoints

| Method | Path            | Returns                                                                                                       |
| ------ | --------------- | ------------------------------------------------------------------------------------------------------------- |
| `GET`  | `/`             | A health check                                                                                                |
| `GET`  | `/navbar`       | The navigation links, in order                                                                                |
| `GET`  | `/about`        | Name, headline, recruiter summary, bio, location, languages, expertise and skill levels by category              |
| `GET`  | `/projects`     | Every place I've worked: stack, pitch, the bullets no case study covers, the titles I held and the dates      |
| `GET`  | `/case-studies` | The work I'd walk a hiring manager through: challenge, approach, outcome and stack                            |
| `GET`  | `/skills`       | The skill cards                                                                                               |
| `GET`  | `/contact`      | Email, mailto link and social profiles                                                                        |
| `GET`  | `/github/repos` | My personal repos (no forks or archived), each pitched by its README's first paragraph. Cached for 10 minutes |
| `GET`  | `/roll`         | A d20 perception check against DC 8, with its own lines for a natural 20 and a natural 1. Fail once and it remembers with a cookie, so a second miss gets a different line |

FastAPI also serves interactive docs at `/docs` and `/redoc` when it runs locally. They're switched off on Railway (detected through the `RAILWAY_ENVIRONMENT_ID` variable Railway sets), so production doesn't hand out a map of the API.

## Security

- CORS only lets the site's own origins read, and only with `GET`. No credentials cross origins.
- Every response carries `nosniff`, `X-Frame-Options: DENY`, HSTS, `Referrer-Policy: no-referrer`, a locked-down `Content-Security-Policy` and a `Permissions-Policy`.
- Each visitor gets 60 requests a minute, then a `429` with `Retry-After`. The visitor is the last address in `X-Forwarded-For`, the one Railway's proxy appends, so a forged header can't dodge the limit. The counter lives in memory, so it resets on deploy and is per instance.
- The `/roll` cookie is `HttpOnly`, `Secure`, `SameSite=Lax` and expires after an hour.

## Running it locally

You need Python 3.13 or older. The pinned `pydantic-core` doesn't build on 3.14 yet.

```bash
python3.13 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

The API runs at `http://localhost:8000`. CORS allows `http://localhost:5173` (the Vite dev server) and the production domain. Add any other origin to `origins` in `main.py`.

`/github/repos` works without credentials, but GitHub only allows 60 anonymous requests an hour. Set `GITHUB_TOKEN` to any personal access token (no scopes needed for public repos) to raise that to 5000.

## Tests

The tests use FastAPI's `TestClient`, which needs `httpx`. It isn't in `requirements.txt` since production doesn't need it, so install it once in your venv:

```bash
pip install httpx
python -m unittest
```

Besides the endpoints, the tests keep the content honest: no em dashes in the copy, every skill icon is one the frontend can render, the main stack shows up in the current role, skill levels stay between one and five, and the skill cards fill complete rows on the page.

## Changing the content

All of the copy lives in `data.py`, and the response shapes are the Pydantic models in `models.py`. Edit the data, run the tests, and the site picks it up on the next request. The site also builds the downloadable resume PDF from these same endpoints, so it never drifts from the page.

Some fields are optional and stay hidden on the site and the resume until they're filled in: each role's `start`, `end` (`"2021"` or `"2021-03"`), `location`, `work_mode` and `team_size`, each case study's `metrics`, each certification's `year` and `verify_url`, each language's `level`, and `open_to` and `work_modes` in the about.

## Deploying

The `Procfile` starts uvicorn on whatever `$PORT` the host provides:

```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```
