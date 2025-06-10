from fastapi import FastAPI
from data import project_data, skills_data
from models import Project, Skill

app = FastAPI(title ="Portfolio API", description="API for my portfolio projects", version="1.0.0")
@app.get("/projects", response_model=list[Project])
def get_projects():
    """
    Retrieve the list of portfolio projects.
    """
    return project_data

@app.get("/skills", response_model=list[Skill])
def get_skills():
    """
    Retrieve the list of skills.
    """
    return skills_data