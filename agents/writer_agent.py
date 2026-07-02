"""Writer agent implementation."""

from llm.gemini_client import GeminiClient
from models.state import ResearchState
from utils.logger import setup_logger
from prompts.writer_prompt import build_writer_prompt
from services.cache_manager import CacheManager

logger = setup_logger(__name__)
class WriterAgent:
    """Agent responsible for creating professional reports."""

    def __init__(self) -> None:
        """Initialize the writer agent."""
        self.llm = GeminiClient()
        self.cache = CacheManager()

    def write_report(self, state: ResearchState) -> ResearchState:
        """Generate the report and update the shared state."""
        logger.info("Generating report...")
        prompt = build_writer_prompt(
        state["research_notes"]
        )

        state["report"] = self.llm.generate(prompt)
        logger.info("Report generated successfully.")
        self.cache.save(
        topic=state["topic"],
        report=state["report"],
        )

        logger.info("Report saved to cache.")

        return state