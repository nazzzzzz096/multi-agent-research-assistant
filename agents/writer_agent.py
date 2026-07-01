"""Writer agent implementation."""

from llm.gemini_client import GeminiClient
from models.state import ResearchState
from utils.logger import setup_logger
from prompts.writer_prompt import build_writer_prompt

logger = setup_logger(__name__)
class WriterAgent:
    """Agent responsible for creating professional reports."""

    def __init__(self) -> None:
        """Initialize the writer agent."""
        self.llm = GeminiClient()

    def write_report(self, state: ResearchState) -> ResearchState:
        """Generate the report and update the shared state."""
        logger.info("Generating report...")
        prompt = build_writer_prompt(
        state["research_notes"]
        )

        state["report"] = self.llm.generate(prompt)
        logger.info("Report generated successfully.")
        return state