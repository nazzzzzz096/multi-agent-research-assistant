"""Application enums."""


from enum import Enum


class Route(str, Enum):
    """Supported routing destinations."""

    RESEARCH = "research"
    GENERAL = "general"
    UNSAFE = "unsafe"


class CacheStatus(str, Enum):
    """Status of a cache lookup."""

    HIT = "hit"
    MISS = "miss"
    STALE = "stale"