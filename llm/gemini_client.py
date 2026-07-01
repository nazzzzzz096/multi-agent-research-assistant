"""Gemini client."""

from google import genai
from google.genai import types

from config import GEMINI_API_KEY, MODEL_NAME, TEMPERATURE


class GeminiClient:
    """Wrapper around the Gemini API."""

    def __init__(self) -> None:
        if not GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY not found.")

        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(self, prompt: str) -> str:
        """Generate a response from Gemini."""

        response = self.client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=TEMPERATURE,
            ),
        )

        return response.text