import os
import json
from dotenv import load_dotenv
from src.memory import Memory

load_dotenv()

class ThoughtToTaskAgent:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.memory = Memory()

    def run(self, user_input: str):
        """
        Real Gemini if available,
        otherwise demo fallback (safe for video & GitHub)
        """

        try:
            if not self.api_key:
                raise RuntimeError("No API key")

            from google import genai
            client = genai.Client(api_key=self.api_key)

            prompt = f"""
You are an autonomous task-planning agent.

User thought:
"{user_input}"

Output ONLY valid JSON with tasks and a daily plan.
"""

            response = client.models.generate_content(
                model="models/gemini-pro-latest",
                contents=prompt
            )

            result = response.text
            self.memory.save_interaction(user_input, result)
            return result

        except Exception:
            # DEMO FALLBACK
            demo = {
                "mode": "demo-agent",
                "input": user_input,
                "tasks": [
                    {
                        "task": "Prepare exam study plan",
                        "category": "Education",
                        "priority": "HIGH",
                        "time_estimate": "2 hours/day",
                        "execution_tip": "Split subjects into daily blocks and use Pomodoro"
                    },
                    {
                        "task": "Update resume",
                        "category": "Career",
                        "priority": "HIGH",
                        "time_estimate": "1–2 hours",
                        "execution_tip": "Highlight recent projects and achievements"
                    },
                    {
                        "task": "Go to the gym",
                        "category": "Health",
                        "priority": "MEDIUM",
                        "time_estimate": "1 hour",
                        "execution_tip": "Fix workout days to build consistency"
                    },
                    {
                        "task": "Clean room",
                        "category": "Personal",
                        "priority": "LOW",
                        "time_estimate": "30 minutes",
                        "execution_tip": "Start with desk and bed"
                    }
                ],
                "daily_plan": "Study in the morning, resume midday, gym evening, clean before sleep."
            }

            self.memory.save_interaction(user_input, demo)
            return demo
