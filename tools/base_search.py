"""Abstract base class for search providers."""

from __future__ import annotations

from abc import ABC, abstractmethod


class BaseSearchProvider(ABC):
    """Interface for search providers."""

    @abstractmethod
    def search(self, query: str) -> str:
        """Search for information.

        Args:
            query: Search query.

        Returns:
            Search results as text.
        """
        raise NotImplementedError