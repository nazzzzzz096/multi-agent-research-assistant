"""Application state models."""

from typing import TypedDict


class ResearchState(TypedDict):
    """Shared state for the research workflow."""

    topic: str
    research_notes: str
    report: str