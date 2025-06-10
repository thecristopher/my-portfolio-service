from pydantic import BaseModel

class Project(BaseModel): 
    title: str
    description: str
    url: str
    technologies: list[str]
    image: str
    
class Skill(BaseModel): 
    title: str
    icon: str
    description: str