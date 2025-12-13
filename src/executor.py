# executor.py
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "models/gemini-pro-latest"

class Executor:
    def __init__(self):
        self.client = genai.Client(api_key=API_KEY)

    def enrich_tasks(self, tasks_json: str):
        prompt = f"""
You are an assistant that enriches tasks.

Tasks:
{tasks_json}

Return ONLY valid JSON in this format:
{{
  "tasks": [
    {{
      "task": "",
      "category": "",
      "priority": "",
      "time_estimate": "",
      "details": ""
    }}
  ]
}}
"""

        response = self.client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        return response.text
