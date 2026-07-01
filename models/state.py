
"""Application state definition."""

from typing import Literal, TypedDict
from models.enums import Route
route: Literal["research", "general", "unsafe"]

class ResearchState(TypedDict):
    """Shared state for the research workflow."""
    topic: str
    research_notes: str
    report: str
    route: Route