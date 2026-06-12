from core.gemini_client import GeminiClient

def test_gemini_client():
    client = GeminiClient()
    prompt = "What is the capital of France?"
    schema = {
        "type": "object",
        "properties": {
            "answer": {"type": "string"}
        },
        "required": ["answer"]
    }
    response = client(prompt, schema)
    assert response
    print("GeminiClient test passed. Response:", response)