"""Research agent implementation."""

from llm.gemini_client import GeminiClient
from models.state import ResearchState
from utils.logger import setup_logger

logger = setup_logger(__name__)
class ResearchAgent:
    """Agent responsible for researching a given topic."""

    def __init__(self) -> None:
        """Initialize the research agent."""
        self.llm = GeminiClient()

    def research(self, state: ResearchState) -> ResearchState:
        """Populate the research notes in the shared state."""
        logger.info("Starting research on topic: %s", state["topic"])
        prompt = f"""
    You are an expert research assistant.

    Research the topic:

    {state["topic"]}

    Provide:
    1. Overview
    2. Key Concepts
    3. Recent Developments
    4. Challenges
    5. References
    """
        
        state["research_notes"] = self.llm.generate(prompt)
        logger.info("Research completed.")
        return state