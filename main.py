from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data import project_data, skills_data
from models import Project, Skill

app = FastAPI(title ="Portfolio API", description="API for my portfolio projects", version="1.0.0")

origins = [
    "http://localhost:5173",  # Local development
    "https://cristophercervantes.com",  # Production URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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