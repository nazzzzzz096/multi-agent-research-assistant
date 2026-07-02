"""Cache management service."""
from __future__ import annotations

import json
from datetime import datetime, timedelta
from pathlib import Path

from models.cache import CacheResult
from models.enums import CacheStatus
from utils.file_utils import slugify
from utils.logger import setup_logger

logger = setup_logger(__name__)
class CacheManager:
    """Manage cached research reports."""

    CACHE_EXPIRY_DAYS = 7

    def __init__(self) -> None:
        """Initialize cache storage."""

        self.report_dir = Path("storage/reports")
        self.metadata_dir = Path("storage/metadata")

        self.report_dir.mkdir(parents=True, exist_ok=True)
        self.metadata_dir.mkdir(parents=True, exist_ok=True)

    def _report_path(self, topic: str) -> Path:
        """Return the report file path."""
        return self.report_dir / f"{slugify(topic)}.md"

    def _metadata_path(self, topic: str) -> Path:
        """Return the metadata file path."""
        return self.metadata_dir / f"{slugify(topic)}.json"

    def get(self, topic: str) -> CacheResult:
        """Retrieve a cached report."""

        report_path = self._report_path(topic)
        metadata_path = self._metadata_path(topic)
        logger.info("Checking cache for topic '%s'", topic)
        if not report_path.exists() or not metadata_path.exists():
            logger.info("Cache miss.")
            return CacheResult(status=CacheStatus.MISS)
         
        with metadata_path.open("r", encoding="utf-8") as file:
            metadata = json.load(file)

        created_at = datetime.fromisoformat(metadata["created_at"])

        age = datetime.now() - created_at

        if age > timedelta(days=self.CACHE_EXPIRY_DAYS):
            return CacheResult(
                status=CacheStatus.STALE,
                created_at=created_at,
                metadata=metadata,
            )

        report = report_path.read_text(encoding="utf-8")
        logger.info("Cache hit.")
        return CacheResult(
            status=CacheStatus.HIT,
            report=report,
            created_at=created_at,
            metadata=metadata,
        )

    def save(
    self,
    topic: str,
    report: str,
) -> None:
        """Save a report and its metadata."""

        report_path = self._report_path(topic)
        metadata_path = self._metadata_path(topic)
        logger.info("Saving report for topic '%s'", topic)
        # Save the markdown report
        report_path.write_text(report, encoding="utf-8")

        now = datetime.now().isoformat()

        version = 1

        # If metadata already exists, increment version
        if metadata_path.exists():
            with metadata_path.open("r", encoding="utf-8") as file:
                existing_metadata = json.load(file)

            version = existing_metadata.get("version", 1) + 1
            created_at = existing_metadata["created_at"]
        else:
            created_at = now

        metadata = {
        "topic": topic,
        "created_at": created_at,
        "updated_at": now,
        "version": version,
    }
        
        with metadata_path.open("w", encoding="utf-8") as file:
            json.dump(metadata, file, indent=4)
        logger.info("Report saved successfully.")

    def delete(
    self,
    topic: str,
) -> None:
        """Delete a cached report."""

        report_path = self._report_path(topic)
        metadata_path = self._metadata_path(topic)

        if report_path.exists():
            report_path.unlink()
        logger.info("Deleting cached report '%s'", topic)
        if metadata_path.exists():
           metadata_path.unlink()