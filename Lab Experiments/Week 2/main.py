
from llm_client import generate_response

def main():
    print("=" * 50)
    print("       MY GEN-AI APPLICATION")
    print("=" * 50)
    print("Ask Gemini anything! Type 'exit' to stop.")

    while True:
        prompt = input("\nYou: ").strip()

        if prompt.lower() == "exit":
            print("Thank you for using Gen-AI!")
            break

        if not prompt:
            print("Please enter a question.")
            continue

        try:
            answer = generate_response(prompt)
            print("\nGemini:", answer)
        except Exception as error:
            print("\nError:", error)

if __name__ == "__main__":
    main()
