#!/usr/bin/python3
""" BasicCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    class BasicCache that inherits from
    BaseCaching and is a caching system
    """

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        """
        if (key is not None or item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value
        in self.cache_data linked to key.
        """
        if key is not None:
            return self.cache_data.get(key, None)
