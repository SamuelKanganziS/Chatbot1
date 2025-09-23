import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def get_response(message: str) -> str:
    """
    Generates a response using Google Gemini API.
    """
    try:
        response = genai.chat(
            model="chat-bison-001",  # You can use other Gemini models if needed
            messages=[{"author": "user", "content": message}],
            temperature=0.7
        )
        return response.last
    except Exception as e:
        print("Gemini API error:", e)
        return "Sorry, I couldn't process your request at the moment."
