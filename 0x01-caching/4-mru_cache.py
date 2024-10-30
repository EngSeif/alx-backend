#!/usr/bin/python3
""" BasicCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    class MRUCache that
    inherits from BaseCaching and
    is a caching system
    """

    def __init__(self):
        """
        Constructor of MRUCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Must assign to the dictionary
        self.cache_data the item value
        for the key key.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.order.remove(key)
                self.order.append(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    lru_key = self.order.pop(-1)
                    self.cache_data.pop(lru_key)
                    print(f"DISCARD: {lru_key}")

                self.cache_data[key] = item
                self.order.append(key)

    def get(self, key):
        """
        Must return the value
        in self.cache_data linked to key.
        """
        if key is not None:
            if self.cache_data.get(key, None) is not None:
                self.order.remove(key)
                self.order.append(key)
                return self.cache_data.get(key, None)
        else:
            return None
