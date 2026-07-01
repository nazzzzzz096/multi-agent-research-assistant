"""Router agent."""

from llm.gemini_client import GeminiClient
from models.state import ResearchState
from prompts.router_prompt import build_router_prompt
from utils.logger import setup_logger
from models.enums import Route
logger = setup_logger(__name__)


class RouterAgent:
    """Route incoming queries."""

    def __init__(self) -> None:
        self.llm = GeminiClient()

    def route(self, state: ResearchState) -> ResearchState:
        """Determine where the query should go."""

        logger.info("Classifying user query.")

        prompt = build_router_prompt(state["topic"])

        response = self.llm.generate(prompt).strip().upper()

        if response == "RESEARCH":
            state["route"] = Route.RESEARCH

        elif response == "GENERAL":
            state["route"] = Route.GENERAL

        else:
            state["route"] = Route.UNSAFE

        logger.info("Query routed to %s", state["route"])

        return state