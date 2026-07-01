"""Research prompt templates."""

from __future__ import annotations


def build_research_prompt(
    topic: str,
    search_results: str,
) -> str:
    """Build the research prompt.

    Args:
        topic: Research topic.
        search_results: Results returned by the search provider.

    Returns:
        Formatted prompt.
    """

    return f"""
You are an expert research assistant.

Your task is to create structured research notes.

Topic:
{topic}

Web Search Results:
{search_results}

Instructions:

1. Provide an overview.
2. Explain important concepts.
3. Mention recent developments.
4. Describe challenges.
5. Mention future trends.
6. Mention important references.

Return the answer in a clean markdown format.
"""