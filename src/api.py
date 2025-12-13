from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from src.agent import ThoughtToTaskAgent
import os

app = FastAPI()

agent = ThoughtToTaskAgent()

# index.html to serve 
@app.get("/", response_class=HTMLResponse)
def read_root():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
        return f.read()

# Agent endpoint
@app.post("/run")
def run_agent(payload: dict):
    user_input = payload.get("input", "")
    result = agent.run(user_input)
    return result
