"""Router prompt."""


def build_router_prompt(query: str) -> str:
    """Build the routing prompt."""

    return f"""
You are a routing classifier.

Classify the following query into EXACTLY ONE category.

Categories:

RESEARCH
- Requires collecting or explaining factual information.
- Comparing technologies.
- Scientific topics.
- Latest developments.
- Tutorials.
- Summaries.

GENERAL
- Casual conversation.
- Greetings.
- Jokes.
- Poems.
- Creative writing.
- Small talk.

UNSAFE
- Illegal activities.
- Harmful instructions.
- Malware.
- Explosives.
- Violence.

Return ONLY ONE WORD.

Query:
{query}
"""