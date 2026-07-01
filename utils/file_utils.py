"""File utility functions."""

from __future__ import annotations

import re


def slugify(text: str) -> str:
    """Convert text into a filesystem-safe slug.

    Args:
        text: Input text.

    Returns:
        Filesystem-safe slug.
    """
    text = text.lower().strip()

    text = re.sub(r"[^\w\s-]", "", text)

    text = re.sub(r"[-\s]+", "-", text)

    return text