from pydantic import BaseModel

class Project(BaseModel): 
    name: str
    description: str
    url: str
    technologies: list[str]
    
class Skill(BaseModel): 
    title: str
    icon: str
    description: str