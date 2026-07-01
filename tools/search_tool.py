"""Search tool with fallback support."""

from __future__ import annotations

from tools.gemini_search import GeminiSearchProvider
from tools.tavily_search import TavilySearchProvider
from utils.logger import setup_logger

logger = setup_logger(__name__)


class SearchTool:
    """Search tool with Tavily as primary provider."""

    def __init__(self) -> None:
        self.primary = TavilySearchProvider()
        self.fallback = GeminiSearchProvider()

    def search(self, query: str) -> str:
        """Search using Tavily, fallback to Gemini."""

        try:
            logger.info("Using Tavily search provider.")
            return self.primary.search(query)

        except Exception as error:
            logger.warning(
                "Tavily search failed: %s", error
            )
            logger.info("Falling back to Gemini.")

            return self.fallback.search(query)