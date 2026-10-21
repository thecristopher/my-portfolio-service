from pydantic import BaseModel, Field
from dataclasses import dataclass

# "2021" or "2021-03". the frontend and the resume print whatever precision is there
MONTH_PATTERN = r"^\d{4}(-(0[1-9]|1[0-2]))?$"


@dataclass
class SocialLink:
    id: int
    name: str
    url: str


class Project(BaseModel):
    title: str
    # one line pitch, the card and the resume lead with it
    description: str
    # the longer story, split on blank lines into one paragraph per chapter of the role
    detailed_description: str
    url: str
    technologies: list[str]
    # every title held there, oldest first. the frontend draws each one as a commit in the career log
    roles: list[str] = []
    # resume bullets: what I shipped and what changed because of it
    highlights: list[str] = []
    location: str | None = None
    # "Remote", "Hybrid" or "On site"
    work_mode: str | None = None
    start: str | None = Field(default=None, pattern=MONTH_PATTERN)
    # None while I still work there
    end: str | None = Field(default=None, pattern=MONTH_PATTERN)
    # how many engineers I led there, only for roles where I led people
    team_size: int | None = None
    # older roles render as a compact list instead of a full card
    featured: bool = True


class Metric(BaseModel):
    value: str
    label: str


class CaseStudy(BaseModel):
    slug: str
    title: str
    company: str
    role: str
    # AI, Platform, Frontend or Product, the gallery groups and tints by it
    kind: str
    summary: str
    challenge: str
    approach: list[str]
    outcome: str
    technologies: list[str]
    # numbers that prove the outcome, only once they were measured
    metrics: list[Metric] = []


class Skill(BaseModel):
    title: str
    icon: str
    description: str
    # the duel monster stats the skill card shows while the magician's buff is on
    attack: int = 0
    defense: int = 0
    effect: str = ""


class NavBarItem(BaseModel):
    title: str
    url: str


class SkillLevel(BaseModel):
    name: str
    level: int
    # Languages, Frontend, Backend, Cloud, Data, AI or Delivery, the checkhealth report groups by it
    category: str = "Other"


class Education(BaseModel):
    school: str
    url: str
    location: str
    degree: str
    # the degree's name as it reads on the diploma
    original_name: str
    start_year: int | None = None
    end_year: int | None = None
    highlights: list[str] = []


class Certification(BaseModel):
    name: str
    issuer: str
    level: str
    year: int | None = None
    # a public verification link, like a Credly badge, once there is one
    verify_url: str | None = None


class Language(BaseModel):
    name: str
    # Native, Fluent, Professional or Conversational, None until stated
    level: str | None = None


class Principle(BaseModel):
    title: str
    body: str


class AboutMe(BaseModel):
    title: str
    name: str
    # the line under the name in the hero and at the top of the resume
    headline: str
    # three sentences a recruiter can read in ten seconds, the resume opens with it
    summary: str
    description: str
    role: str
    years_of_experience: int
    location: str
    timezone: str
    # the roles I'm open to, None hides the badge everywhere
    open_to: str | None = None
    work_modes: list[str] = []
    languages: list[Language] = []
    main_stack: list[str]
    editor: str
    # what I'm good at, not which tools: profile.ts prints it and leaves the tools to the skill bars
    expertise: list[str] = []
    principles: list[Principle] = []
    skill_levels: list[SkillLevel]
    education: list[Education] = []
    certifications: list[Certification] = []


class ContactInfo(BaseModel):
    email: str
    mailto: str
    socials: list[SocialLink]


class RollResult(BaseModel):
    roll: int
    # the difficulty class the roll had to meet
    dc: int
    success: bool
    message: str


class GitHubRepo(BaseModel):
    name: str
    url: str
    pitch: str
    language: str | None
    stars: int
    forks: int
    pushed_at: str
