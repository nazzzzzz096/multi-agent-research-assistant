"""Research agent implementation."""

from llm.gemini_client import GeminiClient
from models.state import ResearchState
from utils.logger import setup_logger
from tools.search_tool import SearchTool
from prompts.research_prompt import build_research_prompt

logger = setup_logger(__name__)
class ResearchAgent:
    """Agent responsible for researching a given topic."""

    def __init__(self) -> None:
        """Initialize the research agent."""
        self.llm = GeminiClient()
        self.search_tool = SearchTool()
    def research(self, state: ResearchState) -> ResearchState:
        """Populate the research notes in the shared state."""
        logger.info("Searching the web...")

        search_results = self.search_tool.search(state["topic"])
        prompt = build_research_prompt(
        topic=state["topic"],
        search_results=search_results,
       )
        logger.info("Generating research summary...")
        
        
        state["research_notes"] = self.llm.generate(prompt)
        logger.info("Research completed.")
        return state