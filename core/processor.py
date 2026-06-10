from PIL import Image
from core.gemini_client import GeminiClient

class Processor:

    def __init__(self):
        self.gemini_client = GeminiClient()
    
    def process(self, image: Image):
        # Placeholder for processing logic
        print(f"Processing data: {data}")