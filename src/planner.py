# planner.py
import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "models/gemini-pro-latest"

class Planner:
    def __init__(self):
        self.client = genai.Client(api_key=API_KEY)

    def plan(self, user_input: str):
        prompt = f"""
You are a task-planning agent.

User thought:
"{user_input}"

Return ONLY valid JSON in this format:
{{
  "tasks": [
    {{
      "task": "",
      "category": "",
      "priority": "",
      "time_estimate": ""
    }}
  ]
}}
"""

        response = self.client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        return response.text
