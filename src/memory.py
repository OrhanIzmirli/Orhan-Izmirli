import json
import os


class Memory:
    def __init__(self, file_name="memory.json"):
        self.file_name = file_name
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w") as f:
                json.dump({"history": []}, f, indent=2)

    def load(self):
        with open(self.file_name, "r") as f:
            return json.load(f)

    def save_interaction(self, user_input, output):
        data = self.load()
        data["history"].append({
            "user_input": user_input,
            "output": output
        })
        with open(self.file_name, "w") as f:
            json.dump(data, f, indent=2)
