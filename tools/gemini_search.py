"""Gemini fallback search provider."""

from __future__ import annotations

from llm.gemini_client import GeminiClient
from tools.base_search import BaseSearchProvider
from utils.logger import setup_logger

logger = setup_logger(__name__)


class GeminiSearchProvider(BaseSearchProvider):
    """Fallback search provider using Gemini knowledge."""

    def __init__(self) -> None:
        self.client = GeminiClient()

    def search(self, query: str) -> str:
        """Generate research information using Gemini."""

        logger.warning("Using Gemini as fallback search provider.")

        prompt = f"""
        You are an expert researcher.

        Provide factual information about:

        {query}

        Include:
        - Overview
        - Key concepts
        - Recent developments
        """

        return self.client.generate(prompt)