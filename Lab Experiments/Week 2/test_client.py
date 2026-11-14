
from llm_client import generate_response

def test_gemini_connection():
    response = generate_response("Say Hello in one sentence.")
    
    assert response is not None
    assert len(response.strip()) > 0

if __name__ == "__main__":
    test_gemini_connection()
    print("Gemini API connection test passed!")
