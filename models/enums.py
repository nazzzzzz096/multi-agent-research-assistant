"""Application enums."""

from enum import Enum


class Route(str, Enum):
    """Supported routing destinations."""

    RESEARCH = "research"
    GENERAL = "general"
    UNSAFE = "unsafe"