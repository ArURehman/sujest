from config import config

class GeminiClient:
    def __init__(self, api_key: str):
        self._api_key = config.GEMINI_API_KEY

    def send_request(self, endpoint: str, data: dict):
        # Placeholder for sending a request to the Gemini API
        print(f"Sending request to {endpoint} with data: {data}")