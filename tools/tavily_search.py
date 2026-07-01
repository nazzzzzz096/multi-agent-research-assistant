"""Tavily search provider."""

from __future__ import annotations

from tavily import TavilyClient

from config import TAVILY_API_KEY
from tools.base_search import BaseSearchProvider
from utils.logger import setup_logger

logger = setup_logger(__name__)


class TavilySearchProvider(BaseSearchProvider):
    """Search provider that uses the Tavily API."""

    def __init__(self) -> None:
        """Initialize the Tavily client."""
        if not TAVILY_API_KEY:
            raise ValueError("TAVILY_API_KEY is not configured.")

        self.client = TavilyClient(api_key=TAVILY_API_KEY)

    def search(self, query: str) -> str:
        """Search the web using Tavily.

        Args:
            query: Search query.

        Returns:
            Combined search results.
        """
        logger.info("Searching Tavily for '%s'", query)

        response = self.client.search(
            query=query,
            max_results=5,
        )

        results = response.get("results", [])

        if not results:
            logger.warning("No results returned from Tavily.")
            return ""

        formatted_results = []

        for result in results:
            title = result.get("title", "")
            content = result.get("content", "")
            url = result.get("url", "")

            formatted_results.append(
                f"Title: {title}\n"
                f"Content: {content}\n"
                f"Source: {url}\n"
            )

        logger.info("Retrieved %d search results.", len(results))

        return "\n\n".join(formatted_results)