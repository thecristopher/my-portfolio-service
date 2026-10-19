from pydantic import BaseModel
from dataclasses import dataclass

@dataclass
class SocialLink:
    id: int
    name: str
    url: str

class Project(BaseModel): 
    title: str
    description: str
    detailed_description: str
    url: str
    technologies: list[str]
    # every title held there, oldest first. the frontend draws each one as a commit in the career log
    roles: list[str] = []
    start_year: int | None = None
    # None while I still work there
    end_year: int | None = None
    # older roles render as a compact list instead of a full card
    featured: bool = True
    
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
    # a public verification link, like a Credly badge, once there is one
    verify_url: str | None = None

class AboutMe(BaseModel):
    title: str
    description: str
    role: str
    main_stack: list[str]
    editor: str
    # what I'm good at, not which tools: profile.json prints it and leaves the tools to the skill bars
    expertise: list[str] = []
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
