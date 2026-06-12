from ast import List
from typing import Optional, Dict, Any

from config import config
from google.genai import types
from google import genai

class GeminiClient:
    def __init__(self):
        self._model = config.GEMINI_MODEL
        self._client = genai.Client(api_key=config.GEMINI_API_KEY)
        
    def _create_content_list(self, prompt: str, image_bytes: Optional[bytes] = None, image_mimetype: str = "") -> List:
        contents = [prompt]
        if image_bytes:
            contents.append(types.Part.from_bytes(
                mime_type=image_mimetype,
                data=image_bytes
            ))
        return contents

    def __call__(self, prompt: str, schema: Dict[str, Any], image_bytes: Optional[bytes] = None, image_mimetype: str = "") -> Dict[str, Any]:
        contents = self._create_content_list(prompt, image_mimetype, image_bytes)
        response = self._client.models.generate_content(
            model=self._model,
            contents=contents,
            config={
                "response_mime_type": "application/json",
                "response_schema": schema
            }
        )
        return response