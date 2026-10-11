# my-portfolio-service

The FastAPI backend that feeds [cristophercervantes.com](https://cristophercervantes.com). It serves the bio, work history, skills, navigation and contact info as JSON, plus a d20 roll for a little game on the site.

The frontend lives in [my-portfolio](https://github.com/thecristopher/my-portfolio).

## Endpoints

| Method | Path | Returns |
| --- | --- | --- |
| `GET` | `/` | A health check |
| `GET` | `/navbar` | The navigation links, in order |
| `GET` | `/about` | Bio, role, main stack, editor and skill levels |
| `GET` | `/projects` | Every place I've worked, with stack and description |
| `GET` | `/skills` | The skill cards |
| `GET` | `/contact` | Email, mailto link and social profiles |
| `GET` | `/roll` | A d20 perception check. Fail once and it remembers with a cookie, so a second miss gets a different line |

FastAPI also serves interactive docs at `/docs` and `/redoc` while it runs.

## Running it locally

You need Python 3.13 or older. The pinned `pydantic-core` doesn't build on 3.14 yet.

```bash
python3.13 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

The API runs at `http://localhost:8000`. CORS allows `http://localhost:5173` (the Vite dev server) and the production domain. Add any other origin to `origins` in `main.py`.

## Tests

The tests use FastAPI's `TestClient`, which needs `httpx`. It isn't in `requirements.txt` since production doesn't need it, so install it once in your venv:

```bash
pip install httpx
python -m unittest
```

Besides the endpoints, the tests keep the content honest: no em dashes in the copy, every skill icon is one the frontend can render, the main stack shows up in the current role, skill levels stay between one and five, and the skill cards fill complete rows on the page.

## Changing the content

All of the copy lives in `data.py`, and the response shapes are the Pydantic models in `models.py`. Edit the data, run the tests, and the site picks it up on the next request.

## Deploying

The `Procfile` starts uvicorn on whatever `$PORT` the host provides:

```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```
