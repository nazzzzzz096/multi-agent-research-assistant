"""Safety agent."""

from models.state import ResearchState


class SafetyAgent:
    """Handle unsafe requests."""

    def deny(self, state: ResearchState) -> ResearchState:
        """Return a refusal message."""

        state["report"] = (
            "I'm sorry, but I can't assist with that request."
        )

        return state