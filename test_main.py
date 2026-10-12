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
    "TbSparkles",
    "TbLayoutDashboard",
    "TbDatabase",
    "TbTestPipe",
    "FaAws",
    "SiNextdotjs",
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
        yield skill.effect


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
        self.assertEqual(about_me_data.role, "Tech Lead & Engineering Manager")

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

    def test_main_stack_is_rated_five_out_of_five(self):
        for tech in about_me_data.main_stack:
            self.assertEqual(self.skill_level_map()[tech], 5)

    def test_main_stack_includes_bedrock_and_llms(self):
        self.assertIn("Bedrock", about_me_data.main_stack)
        self.assertIn("LLMs", about_me_data.main_stack)

    def test_skills_include_an_ai_card(self):
        titles = [skill.title for skill in skills_data]
        self.assertIn("AI & LLMs", titles)

    def test_about_and_skills_leave_the_tools_to_the_work_tags(self):
        # the stack already shows in the work tags and the skill bars, so the prose talks about how, not what
        prose = [about_me_data.description, *(skill.description for skill in skills_data)]
        for tool in about_me_data.main_stack + ["Terraform", "Kubernetes", "Lambda", "DynamoDB"]:
            for text in prose:
                self.assertNotIn(tool, text)

    def test_no_sentence_is_said_twice(self):
        sentences = [
            sentence.strip().lower()
            for text in all_copy()
            for sentence in re.split(r"[.!?]\s", text)
            if sentence.strip()
        ]
        self.assertEqual(len(sentences), len(set(sentences)))

    def test_skill_cards_fill_complete_rows_of_three(self):
        self.assertEqual(len(skills_data) % 3, 0)

    def test_skill_levels_split_evenly_into_two_columns(self):
        self.assertEqual(len(about_me_data.skill_levels) % 2, 0)

    def test_featured_roles_come_before_the_earlier_ones(self):
        flags = [project.featured for project in projects_data]
        self.assertEqual(flags, sorted(flags, reverse=True))
        self.assertTrue(projects_data[0].featured)

    def test_projects_list_at_most_sixteen_tools(self):
        for project in projects_data:
            self.assertLessEqual(len(project.technologies), 16)

    def test_skill_levels_stay_a_short_list(self):
        self.assertLessEqual(len(about_me_data.skill_levels), 30)

    def test_education_names_the_degree_both_ways(self):
        school = about_me_data.education[0]
        self.assertEqual(school.school, "Instituto Tecnológico de Tijuana")
        self.assertIn("Computer Systems Engineering", school.degree)
        self.assertEqual(school.original_name, "Ingeniería en Sistemas Computacionales")

    def test_both_aws_certifications_are_listed(self):
        names = [cert.name for cert in about_me_data.certifications]
        self.assertEqual(len(names), 2)
        self.assertTrue(all(name.startswith("AWS Certified") for name in names))

    def test_every_skill_card_has_duel_stats(self):
        for skill in skills_data:
            self.assertGreater(skill.attack, 0)
            self.assertGreater(skill.defense, 0)
            self.assertTrue(skill.effect)

    def test_about_leaves_the_greeting_to_the_hero(self):
        self.assertNotIn("I'm Cristopher", about_me_data.description)

    def test_csharp_and_node_are_top_rated(self):
        self.assertEqual(self.skill_level_map()["C#"], 5)
        self.assertEqual(self.skill_level_map()["Node.js"], 5)

    def test_psl_pitch_names_the_four_products_it_runs(self):
        psl = projects_data[0]
        for product in ["DGPL", "AMI", "IDH", "MEC"]:
            self.assertIn(product, psl.description)

    def test_firstword_lives_in_the_psl_details_not_the_pitch(self):
        psl = projects_data[0]
        self.assertNotIn("FirstWord", psl.title + psl.description)
        self.assertIn("FirstWord", psl.detailed_description)

    def test_every_role_tells_a_longer_story_than_its_pitch(self):
        for project in projects_data:
            self.assertGreater(len(project.detailed_description), len(project.description))

    def test_about_invites_visitors_to_hunt_the_easter_eggs(self):
        self.assertIn("easter eggs", about_me_data.description)

    def test_contact_uses_the_personal_domain_email(self):
        self.assertEqual(contact_info_data.email, "contact@cristophercervantes.com")

    def test_mailto_points_at_the_same_email(self):
        self.assertEqual(contact_info_data.mailto, f"mailto:{contact_info_data.email}")

    def test_contact_only_lists_professional_socials(self):
        names = [social.name for social in contact_info_data.socials]
        self.assertEqual(names, ["LinkedIn", "GitHub", "Instagram"])

    def test_github_points_at_the_personal_profile(self):
        github = next(social for social in contact_info_data.socials if social.name == "GitHub")
        self.assertEqual(github.url, "https://github.com/thecristopher")


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
