import re
import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from data import about_me_data, case_studies_data, contact_info_data, navbar_data, projects_data, skills_data
import main
from main import app
from models import Project

# the roll cookie is Secure, so the test client has to talk https to get it back
client = TestClient(app, base_url="https://testserver")

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

# the visitors who drop by the site while the tests run
CLAIRE_IP = "1.1.1.1"
INDE_IP = "2.2.2.2"
MALENIA_IP = "3.3.3.3"


def all_copy():
    yield about_me_data.description
    yield about_me_data.summary
    yield about_me_data.headline
    for project in projects_data:
        yield project.description
        yield from project.highlights
    for study in case_studies_data:
        yield study.summary
        yield study.challenge
        yield study.outcome
        yield from study.approach
    for skill in skills_data:
        yield skill.title
        yield skill.description
        yield skill.effect


def skill_level_map():
    return {skill.name: skill.level for skill in about_me_data.skill_levels}


class TheCopyReadsWell(unittest.TestCase):
    """Claire reads the whole site out loud to Inde, and every line lands."""

    def test_the_copy_reads_clean_without_em_dashes(self):
        for text in all_copy():
            self.assertNotIn("\u2014", text)

    def test_the_bio_and_the_summary_agree_on_years_of_experience(self):
        self.assertIn(f"{about_me_data.years_of_experience}+ years", about_me_data.description)
        self.assertIn(f"{about_me_data.years_of_experience}+ years", about_me_data.summary)

    def test_the_about_opens_with_a_lead_paragraph_and_keeps_going(self):
        paragraphs = re.split(r"\n\s*\n", about_me_data.description)
        self.assertGreater(len(paragraphs), 1)

    def test_the_about_names_the_current_role(self):
        self.assertEqual(about_me_data.role, "Tech Lead & Engineering Manager")

    def test_the_prose_talks_about_how_and_leaves_the_tools_to_the_tags(self):
        # the stack already shows in the work tags and the skill bars, so the prose talks about how, not what
        prose = [about_me_data.description, *(skill.description for skill in skills_data)]
        for tool in about_me_data.main_stack + ["Terraform", "Kubernetes", "Lambda", "DynamoDB"]:
            for text in prose:
                self.assertNotIn(tool, text)

    def test_every_sentence_in_the_copy_is_said_just_once(self):
        sentences = [
            sentence.strip().lower()
            for text in all_copy()
            for sentence in re.split(r"[.!?]\s", text)
            if sentence.strip()
        ]
        self.assertEqual(len(sentences), len(set(sentences)))

    def test_the_summary_fits_a_recruiter_skim(self):
        self.assertLessEqual(len(about_me_data.summary), 420)

    def test_the_about_leaves_the_greeting_to_the_hero(self):
        self.assertNotIn("I'm Cristopher", about_me_data.description)

    def test_the_about_invites_visitors_to_touch_the_relics(self):
        self.assertIn("relics", about_me_data.description)


class TheSkillsAddUp(unittest.TestCase):
    """Malenia tallies the skill bars and cards, and every number checks out."""

    def test_every_skill_card_wears_an_icon_the_frontend_can_draw(self):
        for skill in skills_data:
            self.assertIn(skill.icon, KNOWN_SKILL_ICONS)

    def test_the_main_stack_shows_up_in_the_current_role(self):
        current_role_stack = projects_data[0].technologies
        for tech in about_me_data.main_stack:
            self.assertIn(tech, current_role_stack)

    def test_skill_levels_stay_between_one_and_five(self):
        for level in skill_level_map().values():
            self.assertIn(level, range(1, 6))

    def test_every_tool_from_the_work_history_has_a_skill_level(self):
        project_tools = {tech for project in projects_data for tech in project.technologies}
        for tool in project_tools:
            self.assertIn(tool, skill_level_map())

    def test_the_main_stack_leads_the_skill_levels(self):
        leading = [skill.name for skill in about_me_data.skill_levels[: len(about_me_data.main_stack)]]
        self.assertEqual(leading, about_me_data.main_stack)

    def test_each_skill_is_listed_only_once(self):
        names = [skill.name for skill in about_me_data.skill_levels]
        self.assertEqual(len(names), len(set(names)))

    def test_the_main_stack_is_rated_five_out_of_five(self):
        for tech in about_me_data.main_stack:
            self.assertEqual(skill_level_map()[tech], 5)

    def test_the_main_stack_includes_bedrock_and_llms(self):
        self.assertIn("Bedrock", about_me_data.main_stack)
        self.assertIn("LLMs", about_me_data.main_stack)

    def test_csharp_and_node_are_top_rated(self):
        self.assertEqual(skill_level_map()["C#"], 5)
        self.assertEqual(skill_level_map()["Node.js"], 5)

    def test_the_skill_cards_include_one_for_ai(self):
        titles = [skill.title for skill in skills_data]
        self.assertIn("AI & LLMs", titles)

    def test_the_skill_cards_fill_complete_rows_of_three(self):
        self.assertEqual(len(skills_data) % 3, 0)

    def test_the_skill_levels_split_evenly_into_two_columns(self):
        self.assertEqual(len(about_me_data.skill_levels) % 2, 0)

    def test_every_skill_level_belongs_to_a_known_category(self):
        known = {"Languages", "Frontend", "Backend", "Cloud & DevOps", "Data", "AI"}
        for skill in about_me_data.skill_levels:
            self.assertIn(skill.category, known, skill.name)

    def test_the_skill_levels_stay_a_short_list(self):
        self.assertLessEqual(len(about_me_data.skill_levels), 30)

    def test_every_skill_card_is_ready_for_a_friendly_duel(self):
        for skill in skills_data:
            self.assertGreater(skill.attack, 0)
            self.assertGreater(skill.defense, 0)
            self.assertTrue(skill.effect)


class TheWorkHistoryHoldsTogether(unittest.TestCase):
    """Inde follows the career from the first job to today and never loses the thread."""

    def test_career_dates_run_forward(self):
        for project in projects_data:
            if project.start and project.end:
                self.assertLessEqual(project.start, project.end)

    def test_only_the_current_job_is_still_open(self):
        # the career log tags the newest commit as HEAD, so no older job may claim "present"
        for project in projects_data[1:]:
            if project.start:
                self.assertIsNotNone(project.end)

    def test_a_date_written_out_in_words_is_asked_to_use_a_year_or_a_month(self):
        with self.assertRaises(ValueError):
            Project(title="Claire and Inde's first date", description="", url="", technologies=[], start="March 2021")

    def test_every_role_has_bullets_or_a_case_study(self):
        # the resume lists a role's own bullets and its case studies, so every role needs at least one of them
        studied = {study.company for study in case_studies_data}
        for project in projects_data:
            self.assertTrue(project.highlights or project.title in studied, project.title)

    def test_no_bullet_repeats_a_case_study(self):
        summaries = " ".join(f"{study.title} {study.summary} {study.outcome}" for study in case_studies_data).lower()
        for project in projects_data:
            for bullet in project.highlights:
                self.assertNotIn(bullet.lower()[:40], summaries)

    def test_resume_bullets_stay_one_line_long(self):
        for project in projects_data:
            for bullet in project.highlights:
                self.assertLessEqual(len(bullet), 120, bullet)
                self.assertFalse(bullet.endswith("."), bullet)

    def test_every_role_has_a_name(self):
        for project in projects_data:
            for role in project.roles:
                self.assertTrue(role.strip())

    def test_featured_roles_come_before_the_earlier_ones(self):
        flags = [project.featured for project in projects_data]
        self.assertEqual(flags, sorted(flags, reverse=True))
        self.assertTrue(projects_data[0].featured)

    def test_each_role_lists_at_most_sixteen_tools(self):
        for project in projects_data:
            self.assertLessEqual(len(project.technologies), 16)

    def test_psl_names_the_products_it_runs(self):
        psl = " ".join(projects_data[0].highlights)
        for product in ["FirstWord", "DGPL", "MEC", "AMI"]:
            self.assertIn(product, psl)

    def test_umbrella_keeps_its_thank_you_to_erika_soto(self):
        umbrella = next(project for project in projects_data if project.title == "Umbrella Seguros")
        self.assertIn("Erika Soto", umbrella.note)


class TheCaseStudiesTellTheWholeStory(unittest.TestCase):
    """Every case study gets a beginning, a middle and a happy ending."""

    def test_every_case_study_names_a_company_from_the_work_history(self):
        companies = {project.title for project in projects_data}
        for study in case_studies_data:
            self.assertIn(study.company, companies)

    def test_case_study_slugs_are_unique_and_url_safe(self):
        slugs = [study.slug for study in case_studies_data]
        self.assertEqual(len(slugs), len(set(slugs)))
        for slug in slugs:
            self.assertRegex(slug, r"^[a-z0-9-]+$")

    def test_case_studies_only_use_tools_with_a_skill_level(self):
        tools = {skill.name for skill in about_me_data.skill_levels}
        for study in case_studies_data:
            for tech in study.technologies:
                self.assertIn(tech, tools)

    def test_every_case_study_tells_its_challenge_approach_and_outcome(self):
        for study in case_studies_data:
            self.assertTrue(study.challenge and study.approach and study.outcome, study.slug)


class TheCredentialsAreInOrder(unittest.TestCase):
    """The diploma and the certifications, framed and hung where everyone can see them."""

    def test_education_names_the_degree_in_english_and_spanish(self):
        school = about_me_data.education[0]
        self.assertEqual(school.school, "Instituto Tecnológico de Tijuana")
        self.assertIn("Computer Systems Engineering", school.degree)
        self.assertEqual(school.original_name, "Ingeniería en Sistemas Computacionales")

    def test_expertise_names_skills_rather_than_tools(self):
        # profile.json prints this, and the tools already have the skill bars
        self.assertTrue(about_me_data.expertise)
        tools = {skill.name for skill in about_me_data.skill_levels}
        for area in about_me_data.expertise:
            self.assertNotIn(area, tools)

    def test_every_certification_says_what_it_covers(self):
        for cert in about_me_data.certifications:
            self.assertTrue(cert.description, cert.name)

    def test_both_aws_certifications_are_listed(self):
        names = [cert.name for cert in about_me_data.certifications]
        self.assertEqual(len(names), 2)
        self.assertTrue(all(name.startswith("AWS Certified") for name in names))


class TheWayInAndTheWayToReachOut(unittest.TestCase):
    """The navbar leads visitors around and the contact card helps them say hello."""

    def test_every_nav_item_points_at_a_section(self):
        for item in navbar_data:
            self.assertRegex(item.url, r"^/#[a-z]+$")

    def test_contact_uses_the_personal_domain_email(self):
        self.assertEqual(contact_info_data.email, "contact@cristophercervantes.com")

    def test_mailto_points_at_the_same_email(self):
        self.assertEqual(contact_info_data.mailto, f"mailto:{contact_info_data.email}")

    def test_contact_lists_only_professional_socials(self):
        names = [social.name for social in contact_info_data.socials]
        self.assertEqual(names, ["LinkedIn", "GitHub", "Instagram"])

    def test_github_points_at_the_personal_profile(self):
        github = next(social for social in contact_info_data.socials if social.name == "GitHub")
        self.assertEqual(github.url, "https://github.com/thecristopher")


class TheWorkEndpointsServeTheStory(unittest.TestCase):
    """Malenia asks the API for the work, and it arrives exactly as written."""

    def setUp(self):
        main._hits.clear()

    def test_case_studies_arrive_in_the_order_they_were_written(self):
        body = client.get("/case-studies").json()
        self.assertEqual([study["slug"] for study in body], [study.slug for study in case_studies_data])

    def test_projects_arrive_with_their_resume_bullets(self):
        body = client.get("/projects").json()
        self.assertEqual(body[0]["highlights"], projects_data[0].highlights)


class DateNightDiceRolls(unittest.TestCase):
    """Claire, Malenia and Inde roll a d20 to pick the next date night spot."""

    def setUp(self):
        client.cookies.clear()

    def test_claire_rolls_an_eighteen_and_passes_the_check(self):
        with patch("main.randint", return_value=18):
            body = client.get("/roll").json()
        self.assertEqual(body, {"roll": 18, "dc": 8, "success": True, "message": "Check passed. Nice roll."})

    def test_malenia_rolls_a_natural_twenty_for_a_critical_success(self):
        with patch("main.randint", return_value=20):
            body = client.get("/roll").json()
        self.assertEqual(body["message"], "Natural 20! Critical success.")
        self.assertTrue(body["success"])

    def test_inde_rolls_a_natural_one_and_gets_the_critical_line(self):
        with patch("main.randint", return_value=1):
            body = client.get("/roll").json()
        self.assertEqual(body["message"], "Natural 1. Critical failure.")
        self.assertFalse(body["success"])

    def test_a_low_first_roll_invites_claire_to_try_again(self):
        with patch("main.randint", return_value=3):
            body = client.get("/roll").json()
        self.assertEqual(body["message"], "Check failed. Roll again?")

    def test_a_second_low_roll_gets_a_fresh_line(self):
        with patch("main.randint", return_value=3):
            client.get("/roll")
            body = client.get("/roll").json()
        self.assertEqual(body["message"], "Failed again. The dice are not on your side.")

    def test_the_roll_cookie_is_kept_safe(self):
        with patch("main.randint", return_value=3):
            cookie = client.get("/roll").headers["set-cookie"]
        for flag in ["HttpOnly", "Secure", "SameSite=lax", "Max-Age=3600"]:
            self.assertIn(flag, cookie)


class MaleniaKeepsTheGates(unittest.TestCase):
    """Malenia watches over the API so every visitor gets a calm, fair visit."""

    def setUp(self):
        main._hits.clear()

    def tearDown(self):
        # leave the next test a fresh allowance
        main._hits.clear()

    def test_every_response_arrives_with_its_security_headers(self):
        headers = client.get("/").headers
        for header, value in main.SECURITY_HEADERS.items():
            self.assertEqual(headers[header], value)

    def test_cors_lets_the_site_read_and_nothing_more(self):
        response = client.options(
            "/projects",
            headers={"Origin": "https://cristophercervantes.com", "Access-Control-Request-Method": "POST"},
        )
        self.assertEqual(response.status_code, 400)
        self.assertNotIn("access-control-allow-credentials", client.get("/", headers={"Origin": "https://cristophercervantes.com"}).headers)

    def test_cors_politely_ignores_wesker_and_other_unknown_origins(self):
        headers = client.get("/", headers={"Origin": "https://wesker.example"}).headers
        self.assertNotIn("access-control-allow-origin", headers)

    def test_an_eager_visitor_is_asked_to_wait_a_moment(self):
        for _ in range(main.RATE_LIMIT_REQUESTS):
            self.assertEqual(client.get("/").status_code, 200)
        response = client.get("/")
        self.assertEqual(response.status_code, 429)
        self.assertEqual(response.headers["Retry-After"], str(main.RATE_LIMIT_WINDOW_SECONDS))

    def test_inde_keeps_their_own_allowance_after_claire_uses_hers(self):
        for _ in range(main.RATE_LIMIT_REQUESTS):
            client.get("/", headers={"X-Forwarded-For": CLAIRE_IP})
        self.assertEqual(client.get("/", headers={"X-Forwarded-For": INDE_IP}).status_code, 200)

    def test_claire_is_still_recognized_behind_a_borrowed_forwarded_for(self):
        for index in range(main.RATE_LIMIT_REQUESTS):
            client.get("/", headers={"X-Forwarded-For": f"10.0.0.{index}, {CLAIRE_IP}"})
        self.assertEqual(client.get("/", headers={"X-Forwarded-For": f"9.9.9.9, {CLAIRE_IP}"}).status_code, 429)

    def test_malenia_gets_a_fresh_allowance_once_the_window_passes(self):
        self.assertFalse(main.is_rate_limited(MALENIA_IP, now=0))
        for _ in range(main.RATE_LIMIT_REQUESTS):
            main.is_rate_limited(MALENIA_IP, now=1)
        self.assertFalse(main.is_rate_limited(MALENIA_IP, now=main.RATE_LIMIT_WINDOW_SECONDS + 1))


if __name__ == "__main__":
    unittest.main()
