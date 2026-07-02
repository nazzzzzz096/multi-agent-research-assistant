"""Cache agent."""

from models.cache import CacheResult
from models.enums import CacheStatus
from models.state import ResearchState
from services.cache_manager import CacheManager
from utils.logger import setup_logger

logger = setup_logger(__name__)


class CacheAgent:
    """Handle cache lookup."""

    def __init__(self) -> None:
        self.cache = CacheManager()

    def lookup(self, state: ResearchState) -> ResearchState:
        """Check whether a cached report exists."""

        logger.info("Checking cache for '%s'", state["topic"])

        result = self.cache.get(state["topic"])

        state["cache_status"] = result.status

        if result.status == CacheStatus.HIT:
            logger.info("Cache hit.")
            state["report"] = result.report or ""

        elif result.status == CacheStatus.STALE:
            logger.info("Cache stale.")

        else:
            logger.info("Cache miss.")

        return state