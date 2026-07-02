from services.cache_manager import CacheManager

cache = CacheManager()

cache.save(
    topic="LLMs",
    report="# Hello\n\nThis is a cached report."
)

result = cache.get("LLMs")

print(result.status)
print(result.report)
print(result.metadata)