from services.cache_manager import CacheManager

cache = CacheManager()

result = cache.get("LangGraph")

print(result)
print(result.status)