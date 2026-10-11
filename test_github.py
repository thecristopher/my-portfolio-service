import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

import github
from main import app

client = TestClient(app)


def raw_repo(name, **extra):
    return {
        "name": name,
        "html_url": f"https://github.com/thecristopher/{name}",
        "description": None,
        "language": "Python",
        "stargazers_count": 0,
        "forks_count": 0,
        "pushed_at": "2026-01-01T00:00:00Z",
        "fork": False,
        "archived": False,
        **extra,
    }


class ReadmePitchTests(unittest.TestCase):
    def test_skips_the_title_and_returns_the_first_paragraph(self):
        pitch = github.readme_pitch("# merchant-shop\n\nWhat're ya buyin'? Rare guns at fair prices.")
        self.assertEqual(pitch, "What're ya buyin'? Rare guns at fair prices.")

    def test_joins_a_paragraph_that_wraps_across_lines(self):
        self.assertEqual(github.readme_pitch("Ranni's plan\nspans many nights."), "Ranni's plan spans many nights.")

    def test_ignores_code_blocks(self):
        self.assertEqual(github.readme_pitch("```\nrm -rf umbrella\n```\n\nCleans up the lab."), "Cleans up the lab.")

    def test_keeps_link_text_and_drops_the_markdown_around_it(self):
        self.assertEqual(github.readme_pitch("Built for **Leon** by [Ada](https://ada.wong)."), "Built for Leon by Ada.")

    def test_skips_badges(self):
        pitch = github.readme_pitch("[![build](https://x.y/b.svg)](https://x.y)\n\nMaidenless and proud.")
        self.assertEqual(pitch, "Maidenless and proud.")

    def test_trims_a_long_pitch_at_a_word_with_an_ellipsis(self):
        self.assertTrue(github.readme_pitch("Tarnished " * 40).endswith("Tarnished…"))

    def test_returns_nothing_when_the_readme_is_only_a_title(self):
        self.assertEqual(github.readme_pitch("# govee-sync"), "")


class RepoPitchTests(unittest.TestCase):
    def test_prefers_the_readme_over_the_github_description(self):
        pitch = github.repo_pitch("# merchant-shop\n\nStranger, stranger, now that's a weapon.", "Old shop")
        self.assertEqual(pitch, "Stranger, stranger, now that's a weapon.")

    def test_falls_back_to_the_description_when_the_readme_has_no_paragraph(self):
        self.assertEqual(github.repo_pitch("# roundtable-hold", "A hub for the Tarnished"), "A hub for the Tarnished")

    def test_falls_back_to_the_description_when_there_is_no_readme(self):
        self.assertEqual(github.repo_pitch("", "Jill's master of unlocking"), "Jill's master of unlocking")

    def test_admits_defeat_when_there_is_neither(self):
        self.assertEqual(github.repo_pitch("", None), github.NO_PITCH)


class PickPersonalReposTests(unittest.TestCase):
    def names(self, repos):
        return [repo["name"] for repo in github.pick_personal_repos(repos)]

    def test_drops_forks(self):
        self.assertEqual(self.names([raw_repo("leon"), raw_repo("ada-fork", fork=True)]), ["leon"])

    def test_drops_archived_repos(self):
        self.assertEqual(self.names([raw_repo("melina"), raw_repo("old-ranni", archived=True)]), ["melina"])

    def test_puts_the_most_starred_first(self):
        repos = [raw_repo("chris", stargazers_count=1), raw_repo("jill", stargazers_count=9)]
        self.assertEqual(self.names(repos), ["jill", "chris"])

    def test_breaks_star_ties_by_most_recent_push(self):
        repos = [
            raw_repo("radahn", pushed_at="2026-01-01T00:00:00Z"),
            raw_repo("malenia", pushed_at="2026-05-01T00:00:00Z"),
        ]
        self.assertEqual(self.names(repos), ["malenia", "radahn"])


class GetReposCacheTests(unittest.TestCase):
    def setUp(self):
        github._cache.update(repos=None, fetched_at=0.0)

    def test_reuses_the_list_inside_the_cache_window(self):
        with patch("github.fetch_repos", return_value=["leon"]) as fetch:
            github.get_repos(now=1000)
            github.get_repos(now=1000 + github.CACHE_SECONDS - 1)
        self.assertEqual(fetch.call_count, 1)

    def test_refetches_once_the_cache_expires(self):
        with patch("github.fetch_repos", return_value=["leon"]) as fetch:
            github.get_repos(now=1000)
            github.get_repos(now=1000 + github.CACHE_SECONDS)
        self.assertEqual(fetch.call_count, 2)

    def test_serves_the_stale_list_when_github_fails(self):
        github._cache.update(repos=["ashley"], fetched_at=0.0)
        with patch("github.fetch_repos", side_effect=OSError):
            self.assertEqual(github.get_repos(now=99999), ["ashley"])


class GitHubReposEndpointTests(unittest.TestCase):
    def setUp(self):
        github._cache.update(repos=None, fetched_at=0.0)

    def test_pitches_each_repo_with_its_readme(self):
        repo = raw_repo("canon-open-webcam", description="Old blurb")
        with patch("github.github_get", return_value=f"[{github.json.dumps(repo)}]"), \
             patch("github.fetch_readme", return_value="# canon\n\nUse a Canon as a webcam."):
            body = client.get("/github/repos").json()
        self.assertEqual(body[0]["pitch"], "Use a Canon as a webcam.")

    def test_answers_502_when_github_is_down_and_nothing_is_cached(self):
        with patch("github.github_get", side_effect=OSError):
            response = client.get("/github/repos")
        self.assertEqual(response.status_code, 502)


if __name__ == "__main__":
    unittest.main()
