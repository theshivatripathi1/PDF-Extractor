import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"
MODEL = "gemini-2.5-flash"  # <-- CONFIRMED WORKING MODEL

def ask_gemini(context: str, question: str) -> str:
    if not API_KEY:
        return "Gemini error: API key not found"

    prompt = f"""
You are a document question-answering assistant.

Answer the question using ONLY the document below.
If the answer is not present in the document, say:
"Answer not found in the document."

Document:
{context}

Question:
{question}
"""

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    url = f"{BASE_URL}/{MODEL}:generateContent?key={API_KEY}"

    response = requests.post(url, json=payload, timeout=30)

    if response.status_code != 200:
        return f"Gemini error: {response.text}"

    data = response.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]
