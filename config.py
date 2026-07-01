"""Application configuration."""

from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY: str | None = os.getenv("GEMINI_API_KEY")

MODEL_NAME = "gemini-2.5-flash"
TEMPERATURE = 0.2