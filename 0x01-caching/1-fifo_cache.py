#!/usr/bin/python3
""" BasicCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    class FIFOCache that
    inherits from BaseCaching and
    is a caching system
    """

    def __init__(self):
        """
        Constructor of FifoCache
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
                    firstKey = list(self.cache_data.keys())[0]
                    print(f"DISCARD: {firstKey}")
                    self.cache_data.pop(firstKey)
            self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value
        in self.cache_data linked to key.
        """
        return self.cache_data.get(key, None)
