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
    """Claire keeps her love notes for Inde in READMEs, and the pitch finds the sweetest line."""

    def test_skips_the_title_and_finds_the_first_paragraph(self):
        pitch = github.readme_pitch("# love-notes\n\nLittle notes Claire leaves for Inde before every mission.")
        self.assertEqual(pitch, "Little notes Claire leaves for Inde before every mission.")

    def test_joins_a_paragraph_that_wraps_across_lines(self):
        pitch = github.readme_pitch("Malenia's garden\nblooms again every spring.")
        self.assertEqual(pitch, "Malenia's garden blooms again every spring.")

    def test_looks_past_code_blocks_to_the_prose(self):
        pitch = github.readme_pitch("```\nnpm run playlist\n```\n\nShares the playlist Inde made for Malenia.")
        self.assertEqual(pitch, "Shares the playlist Inde made for Malenia.")

    def test_keeps_link_text_and_lets_the_markdown_go(self):
        pitch = github.readme_pitch("Built for **Inde** by [Claire](https://claire.redfield).")
        self.assertEqual(pitch, "Built for Inde by Claire.")

    def test_looks_past_badges_to_the_prose(self):
        pitch = github.readme_pitch("[![build](https://x.y/b.svg)](https://x.y)\n\nTorrent found his way home.")
        self.assertEqual(pitch, "Torrent found his way home.")

    def test_trims_a_long_pitch_at_a_word_with_an_ellipsis(self):
        self.assertTrue(github.readme_pitch("Graceful " * 40).endswith("Graceful…"))

    def test_returns_an_empty_pitch_while_the_readme_is_only_a_title(self):
        self.assertEqual(github.readme_pitch("# anniversary-playlist"), "")


class RepoPitchTests(unittest.TestCase):
    """Every repo gets a pitch, whether it comes from the README or the About box."""

    def test_prefers_the_readme_over_the_github_description(self):
        pitch = github.repo_pitch("# love-notes\n\nEvery note Claire wrote, kept safe in one place.", "Old notes")
        self.assertEqual(pitch, "Every note Claire wrote, kept safe in one place.")

    def test_uses_the_description_when_the_readme_has_only_a_title(self):
        pitch = github.repo_pitch("# date-night", "Where Malenia and Inde plan their next date")
        self.assertEqual(pitch, "Where Malenia and Inde plan their next date")

    def test_uses_the_description_when_there_is_no_readme_yet(self):
        pitch = github.repo_pitch("", "Rebecca's field kit, patched and ready")
        self.assertEqual(pitch, "Rebecca's field kit, patched and ready")

    def test_offers_the_friendly_placeholder_when_there_is_neither(self):
        self.assertEqual(github.repo_pitch("", None), github.NO_PITCH)


class PickPersonalReposTests(unittest.TestCase):
    """Only the repos that are truly Cristopher's make it onto the shelf, best loved first."""

    def names(self, repos):
        return [repo["name"] for repo in github.pick_personal_repos(repos)]

    def test_leaves_forks_off_the_shelf(self):
        repos = [raw_repo("claire-and-inde"), raw_repo("leon-fork", fork=True)]
        self.assertEqual(self.names(repos), ["claire-and-inde"])

    def test_leaves_archived_repos_off_the_shelf(self):
        repos = [raw_repo("melina"), raw_repo("godrick-archive", archived=True)]
        self.assertEqual(self.names(repos), ["melina"])

    def test_puts_the_most_starred_first(self):
        repos = [raw_repo("chris", stargazers_count=1), raw_repo("jill", stargazers_count=9)]
        self.assertEqual(self.names(repos), ["jill", "chris"])

    def test_breaks_star_ties_by_the_most_recent_push(self):
        repos = [
            raw_repo("radahn", pushed_at="2026-01-01T00:00:00Z"),
            raw_repo("malenia", pushed_at="2026-05-01T00:00:00Z"),
        ]
        self.assertEqual(self.names(repos), ["malenia", "radahn"])


class MainLanguagesTests(unittest.TestCase):
    """A repo shows every language that carries real weight, like the songs that made the anniversary playlist."""

    def test_keeps_both_languages_of_claires_webcam_app_biggest_first(self):
        self.assertEqual(github.main_languages({"Rust": 4000, "Swift": 6000}), ["Swift", "Rust"])

    def test_leaves_out_a_language_under_a_tenth_of_the_code(self):
        self.assertEqual(github.main_languages({"Lua": 9500, "Shell": 500}), ["Lua"])

    def test_caps_malenias_polyglot_repo_at_three_languages(self):
        counts = {"Python": 400, "Rust": 300, "Go": 200, "Lua": 100}
        self.assertEqual(github.main_languages(counts), ["Python", "Rust", "Go"])

    def test_returns_no_languages_for_inde_readme_only_repo(self):
        self.assertEqual(github.main_languages({}), [])


class GetReposCacheTests(unittest.TestCase):
    """The repo list is kept close at hand, like a playlist saved for the drive home."""

    def setUp(self):
        github._cache.update(repos=None, fetched_at=0.0)

    def test_reuses_the_list_inside_the_cache_window(self):
        with patch("github.fetch_repos", return_value=["inde-playlist"]) as fetch:
            github.get_repos(now=1000)
            github.get_repos(now=1000 + github.CACHE_SECONDS - 1)
        self.assertEqual(fetch.call_count, 1)

    def test_fetches_a_fresh_list_once_the_cache_expires(self):
        with patch("github.fetch_repos", return_value=["inde-playlist"]) as fetch:
            github.get_repos(now=1000)
            github.get_repos(now=1000 + github.CACHE_SECONDS)
        self.assertEqual(fetch.call_count, 2)

    def test_serves_the_last_good_list_while_github_recovers(self):
        github._cache.update(repos=["rennala"], fetched_at=0.0)
        with patch("github.fetch_repos", side_effect=OSError):
            self.assertEqual(github.get_repos(now=99999), ["rennala"])


class GitHubReposEndpointTests(unittest.TestCase):
    """The endpoint hands the site each repo with its README pitch ready to show."""

    def setUp(self):
        github._cache.update(repos=None, fetched_at=0.0)

    def test_pitches_each_repo_with_its_readme(self):
        repo = raw_repo("anniversary-album", description="Old blurb")
        readme = "# anniversary-album\n\nEvery photo from Claire and Inde's anniversary trip."
        with patch("github.github_get", return_value=f"[{github.json.dumps(repo)}]"), \
             patch("github.fetch_readme", return_value=readme), \
             patch("github.fetch_languages", return_value={}):
            body = client.get("/github/repos").json()
        self.assertEqual(body[0]["pitch"], "Every photo from Claire and Inde's anniversary trip.")

    def test_lists_every_main_language_of_the_repo(self):
        repo = raw_repo("canon-webcam", language="Swift")
        with patch("github.github_get", return_value=f"[{github.json.dumps(repo)}]"), \
             patch("github.fetch_readme", return_value=""), \
             patch("github.fetch_languages", return_value={"Swift": 6000, "Rust": 4000}):
            body = client.get("/github/repos").json()
        self.assertEqual(body[0]["languages"], ["Swift", "Rust"])

    def test_answers_502_while_github_rests_and_nothing_is_cached_yet(self):
        with patch("github.github_get", side_effect=OSError):
            response = client.get("/github/repos")
        self.assertEqual(response.status_code, 502)


if __name__ == "__main__":
    unittest.main()
