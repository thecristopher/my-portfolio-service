import json
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request, urlopen

from models import GitHubRepo

GITHUB_USER = "thecristopher"
API_URL = "https://api.github.com"
CACHE_SECONDS = 600
PITCH_MAX_CHARS = 220
NO_PITCH = "Still writing the README for this one."
# a language has to be at least a tenth of the code to make the card, and three is plenty for one card
LANGUAGE_MIN_SHARE = 0.1
MAX_LANGUAGES = 3

# headings, badges, html, tables, lists and quotes aren't a pitch, so a paragraph has to start with plain text
PROSE_START = re.compile(r"^[A-Za-z0-9*_`\"'(]")

_cache = {"repos": None, "fetched_at": 0.0}


def strip_markdown(text):
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_`]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def is_prose(line):
    return bool(PROSE_START.match(line)) and not line.startswith("[![")


def readme_pitch(markdown):
    """The first real paragraph of a README, so the card says what the repo actually does."""
    in_code = False
    paragraph = []
    for raw_line in (markdown or "").split("\n"):
        line = raw_line.strip()
        if line.startswith("```"):
            in_code = not in_code
        elif in_code:
            continue
        elif paragraph and not line:
            break
        elif paragraph or is_prose(line):
            paragraph.append(line)

    pitch = strip_markdown(" ".join(paragraph))
    if len(pitch) <= PITCH_MAX_CHARS:
        return pitch
    return pitch[: pitch.rfind(" ", 0, PITCH_MAX_CHARS)] + "…"


def repo_pitch(readme, description):
    # the README is what actually gets kept up to date, so it beats the one liner in GitHub's About box
    return readme_pitch(readme) or description or NO_PITCH


def main_languages(byte_counts):
    """The languages that make up a real share of a repo, biggest first, so a Swift and Rust app shows both."""
    total = sum(byte_counts.values())
    if not total:
        return []
    ranked = sorted(byte_counts.items(), key=lambda item: item[1], reverse=True)
    return [name for name, size in ranked if size / total >= LANGUAGE_MIN_SHARE][:MAX_LANGUAGES]


def pick_personal_repos(repos):
    # forks and archived repos aren't really mine anymore, the rest go by stars, then by what I touched last
    personal = [repo for repo in repos if not repo["fork"] and not repo["archived"]]
    personal.sort(key=lambda repo: repo["pushed_at"], reverse=True)
    personal.sort(key=lambda repo: repo["stargazers_count"], reverse=True)
    return personal


def github_get(path, accept="application/vnd.github+json"):
    headers = {"Accept": accept, "User-Agent": GITHUB_USER}
    # a token lifts the limit from 60 to 5000 requests an hour, but public data works without one
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urlopen(Request(f"{API_URL}{path}", headers=headers), timeout=10) as response:
        return response.read().decode("utf-8")


def fetch_readme(repo_name):
    try:
        return github_get(f"/repos/{GITHUB_USER}/{repo_name}/readme", accept="application/vnd.github.raw")
    except OSError:
        return ""


def fetch_languages(repo_name):
    try:
        return json.loads(github_get(f"/repos/{GITHUB_USER}/{repo_name}/languages"))
    except (OSError, ValueError):
        return {}


def to_github_repo(repo, readme, byte_counts=None):
    return GitHubRepo(
        name=repo["name"],
        url=repo["html_url"],
        pitch=repo_pitch(readme, repo["description"]),
        language=repo["language"],
        languages=main_languages(byte_counts or {}),
        stars=repo["stargazers_count"],
        forks=repo["forks_count"],
        pushed_at=repo["pushed_at"],
    )


def fetch_repos():
    repos = pick_personal_repos(json.loads(github_get(f"/users/{GITHUB_USER}/repos?per_page=100&sort=pushed")))
    names = [repo["name"] for repo in repos]
    with ThreadPoolExecutor() as pool:
        readmes = list(pool.map(fetch_readme, names))
        languages = list(pool.map(fetch_languages, names))
    return [to_github_repo(repo, readme, counts) for repo, readme, counts in zip(repos, readmes, languages)]


def get_repos(now=None):
    """Personal repos with a README pitch, cached so every visitor doesn't spend our GitHub rate limit."""
    now = time.time() if now is None else now
    is_fresh = _cache["repos"] is not None and now - _cache["fetched_at"] < CACHE_SECONDS
    if is_fresh:
        return _cache["repos"]

    try:
        _cache["repos"] = fetch_repos()
        _cache["fetched_at"] = now
    except OSError:
        # GitHub hiccupped, an old list beats an empty section
        if _cache["repos"] is None:
            raise
    return _cache["repos"]
