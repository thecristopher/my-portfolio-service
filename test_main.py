import re
import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from data import about_me_data, contact_info_data, projects_data, skills_data
from main import app

client = TestClient(app)

# icon names the frontend knows how to render
KNOWN_SKILL_ICONS = {
    "TbUserCode",
    "FaAws",
    "SiNextdotjs",
    "SiAmazondynamodb",
    "SiNeovim",
    "GrShieldSecurity",
}


def all_copy():
    yield about_me_data.description
    for project in projects_data:
        yield project.description
        yield project.detailed_description
    for skill in skills_data:
        yield skill.title
        yield skill.description


class CopyTests(unittest.TestCase):
    def test_copy_has_no_em_dashes(self):
        for text in all_copy():
            self.assertNotIn("\u2014", text)

    def test_about_mentions_years_for_the_hero_stat(self):
        self.assertRegex(about_me_data.description, r"\d+\+? years")

    def test_about_has_a_lead_paragraph_and_more(self):
        paragraphs = re.split(r"\n\s*\n", about_me_data.description)
        self.assertGreater(len(paragraphs), 1)

    def test_every_skill_uses_an_icon_the_frontend_knows(self):
        for skill in skills_data:
            self.assertIn(skill.icon, KNOWN_SKILL_ICONS)

    def test_about_names_the_current_role(self):
        self.assertEqual(about_me_data.role, "Engineering Manager")

    def test_main_stack_is_used_in_the_current_role(self):
        current_role_stack = projects_data[0].technologies
        for tech in about_me_data.main_stack:
            self.assertIn(tech, current_role_stack)

    def skill_level_map(self):
        return {skill.name: skill.level for skill in about_me_data.skill_levels}

    def test_skill_levels_stay_between_one_and_five(self):
        for level in self.skill_level_map().values():
            self.assertIn(level, range(1, 6))

    def test_every_project_tool_has_a_skill_level(self):
        project_tools = {tech for project in projects_data for tech in project.technologies}
        for tool in project_tools:
            self.assertIn(tool, self.skill_level_map())

    def test_main_stack_leads_the_skill_levels(self):
        leading = [skill.name for skill in about_me_data.skill_levels[: len(about_me_data.main_stack)]]
        self.assertEqual(leading, about_me_data.main_stack)

    def test_no_skill_is_listed_twice(self):
        names = [skill.name for skill in about_me_data.skill_levels]
        self.assertEqual(len(names), len(set(names)))

    def test_csharp_and_node_are_top_rated(self):
        self.assertEqual(self.skill_level_map()["C#"], 5)
        self.assertEqual(self.skill_level_map()["Node.js"], 5)

    def test_contact_uses_the_personal_domain_email(self):
        self.assertEqual(contact_info_data.email, "contact@cristophercervantes.com")

    def test_mailto_points_at_the_same_email(self):
        self.assertEqual(contact_info_data.mailto, f"mailto:{contact_info_data.email}")

    def test_contact_only_lists_professional_socials(self):
        names = [social.name for social in contact_info_data.socials]
        self.assertEqual(names, ["LinkedIn", "Instagram"])


class RollTests(unittest.TestCase):
    def setUp(self):
        client.cookies.clear()

    def test_high_roll_passes_the_check(self):
        with patch("main.randint", return_value=18):
            body = client.get("/roll").json()
        self.assertEqual(body, {"roll": 18, "success": True, "message": "Check passed. Nice roll."})

    def test_first_low_roll_invites_another_try(self):
        with patch("main.randint", return_value=3):
            body = client.get("/roll").json()
        self.assertEqual(body["message"], "Check failed. Roll again?")

    def test_second_low_roll_gets_a_different_line(self):
        with patch("main.randint", return_value=3):
            client.get("/roll")
            body = client.get("/roll").json()
        self.assertEqual(body["message"], "Failed again. The dice are not on your side.")


if __name__ == "__main__":
    unittest.main()
