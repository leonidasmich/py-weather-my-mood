import requests
import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_API", "http://YOUR_VPS_IP:11434/api/generate")

def extract_mood(text: str) -> str:
    prompt = f"What is the overall emotional mood of the following text? Respond with one word.\n\nText: {text}"

    try:
        response = requests.post(OLLAMA_URL, json={
            "model": "tinyllama",
            "prompt": prompt,
            "stream": False
        }, timeout=10)

        if response.status_code == 200:
            reply = response.json()["response"].strip()
            mood = reply.split()[0].capitalize()
            return mood
        else:
            print("Ollama error:", response.text)
            return "Unknown"
    except Exception as e:
        print("Ollama exception:", e)
        return "Unknown"
