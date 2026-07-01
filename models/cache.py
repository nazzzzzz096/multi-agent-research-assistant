"""Cache models."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from models.enums import CacheStatus


@dataclass
class CacheResult:
    """Represents the result of a cache lookup."""

    status: CacheStatus
    report: str | None = None
    created_at: datetime | None = None
    metadata: dict | None = None