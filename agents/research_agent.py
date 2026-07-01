"""Research agent implementation."""

from llm.gemini_client import GeminiClient
from models.state import ResearchState

class ResearchAgent:
    """Agent responsible for researching a given topic."""

    def __init__(self) -> None:
        """Initialize the research agent."""
        self.llm = GeminiClient()

    def research(self, state: ResearchState) -> ResearchState:
        """Populate the research notes in the shared state."""

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

        return state