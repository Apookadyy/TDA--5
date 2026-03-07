import time

# Simple in-memory cache dictionary
cache_store = {}

# Cache expiration time (seconds)
CACHE_EXPIRY = 60


def cache_data(key, value):
    """
    Store data in cache with timestamp
    """
    cache_store[key] = {
        "value": value,
        "timestamp": time.time()
    }
    return value


def get_cached_data(key):
    """
    Retrieve data from cache if not expired
    """
    if key in cache_store:

        cached_item = cache_store[key]
        current_time = time.time()

        # Check if cache expired
        if current_time - cached_item["timestamp"] < CACHE_EXPIRY:
            print("Cache Hit")
            return cached_item["value"]

        else:
            print("Cache Expired")
            del cache_store[key]

    print("Cache Miss")
    return None


def clear_cache():
    """
    Clear all cache entries
    """
    cache_store.clear()
    print("Cache Cleared")


def cache_stats():
    """
    Show cache statistics
    """
    return {
        "total_cached_items": len(cache_store),
        "keys": list(cache_store.keys())
    }