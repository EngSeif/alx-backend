#!/usr/bin/python3
""" BasicCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    class LIFOCache that
    inherits from BaseCaching and
    is a caching system
    """

    def __init__(self):
        """
        Constructor of LIFOCache
        """
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary
        self.cache_data the item value
        for the key key.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.get(key) is None:
                    lastKey = list(self.cache_data.keys())[-1]
                    print(f"DISCARD: {lastKey}")
                    self.cache_data.pop(lastKey)
            self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value
        in self.cache_data linked to key.
        """
        return self.cache_data.get(key, None)
