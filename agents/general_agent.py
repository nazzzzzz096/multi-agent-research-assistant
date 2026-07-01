"""General conversation agent."""

from llm.gemini_client import GeminiClient
from models.state import ResearchState
from utils.logger import setup_logger

logger = setup_logger(__name__)


class GeneralAgent:
    """Handle general conversations."""

    def __init__(self) -> None:
        self.llm = GeminiClient()

    def respond(self, state: ResearchState) -> ResearchState:
        """Respond to general queries."""

        logger.info("Handling general conversation.")

        prompt = f"""
        You are a friendly AI assistant.

        Respond naturally to:

        {state["topic"]}
        """

        state["report"] = self.llm.generate(prompt)

        return state