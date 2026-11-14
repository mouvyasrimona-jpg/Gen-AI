import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env file
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Error: Gemini API key not found!")
    exit()

# Create Gemini client
client = genai.Client(api_key=API_KEY)

print("=" * 50)
print("       MY FIRST LLM API APPLICATION")
print("=" * 50)

print("Ask Gemini anything! Type 'exit' to stop.")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Thank you for using my application!")
        break

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )

        print("\nGemini:", response.text)

    except Exception as e:
        print("Error:", e)