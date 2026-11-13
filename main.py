
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found in .env file")

client = genai.Client(api_key=api_key)

print("=" * 50)
print("       MY FIRST GENAI APPLICATION")
print("=" * 50)

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    try:
        response = client.models.generate_content(
           model="gemini-3.8-flash",
            contents=question
        )
        print("\nGemini:", response.text)

    except Exception as e:
        print("Error:", e)
