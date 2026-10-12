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
    image: str
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

class AboutMe(BaseModel):
    title: str
    description: str
    role: str
    main_stack: list[str]
    editor: str
    skill_levels: list[SkillLevel]
    
class ContactInfo(BaseModel):
    email: str
    mailto: str
    socials: list[SocialLink]
    
class RollResult(BaseModel):
    roll: int
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
