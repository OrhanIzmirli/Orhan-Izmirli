# src/list_models.py

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not found in .env")

    client = genai.Client(api_key=api_key)

    print("\nModels that support generateContent:\n")
    for m in client.models.list():
        if "generateContent" in (m.supported_actions or []):
            print(m.name)

if __name__ == "__main__":
    main()
