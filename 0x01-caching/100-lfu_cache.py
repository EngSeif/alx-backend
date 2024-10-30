#!/usr/bin/python3
""" BasicCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    class LFUCache that
    inherits from BaseCaching and
    is a caching system
    """

    def __init__(self):
        """
        Constructor of LFUCache
        """
        super().__init__()
        self.order = []
        self.freq = {}

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
                self.freq[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    min_key = min(self.freq, key=self.freq.get)
                    min_value = self.freq[min_key]
                    keys_with_min_value = [
                        k for k, v in self.freq.items() if v == min_value
                    ]
                    if len(keys_with_min_value) > 1:
                        min_indx = min([
                            self.order.index(k) for k in keys_with_min_value
                        ])
                        min_key = self.order[min_indx]
                        self.freq.pop(min_key)
                        self.cache_data.pop(min_key)
                        self.order.remove(min_key)
                        print(f"DISCARD: {min_key}")
                    else:
                        self.freq.pop(min_key)
                        self.cache_data.pop(min_key)
                        self.order.remove(min_key)
                        print(f"DISCARD: {min_key}")

                self.cache_data[key] = item
                self.order.append(key)
                self.freq[key] = 1

    def get(self, key):
        """
        Must return the value
        in self.cache_data linked to key.
        """
        if key is not None:
            if self.cache_data.get(key, None) is not None:
                self.order.remove(key)
                self.order.append(key)
                self.freq[key] += 1
                return self.cache_data.get(key, None)
        else:
            return None
