"""Writer prompt templates."""

from __future__ import annotations


def build_writer_prompt(
    research_notes: str,
) -> str:
    """Build the writer prompt."""

    return f"""
You are a technical writer.

Convert the following research notes into a professional markdown report.

The report must contain:

# Title

## Executive Summary

## Key Concepts

## Recent Developments

## Challenges

## Future Scope

## Conclusion

Research Notes:

{research_notes}
"""