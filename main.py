from fastapi import FastAPI
from data import portfolio_data
from models import Project

app = FastAPI(title ="Portfolio API", description="API for my portfolio projects", version="1.0.0")
@app.get("/projects", response_model=list[Project])
def get_projects():
    """
    Retrieve the list of portfolio projects.
    """
    return portfolio_data