from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

PROMPT = input(str("Prompt: "))

google_client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

response = google_client.models.generate_content(
    model="gemini-2.0-flash", contents=PROMPT
)

print(response.text)