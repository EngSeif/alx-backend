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
        self.freq = {
            i: 0 for i in range(0, BaseCaching.MAX_ITEMS)
        }

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
                keys_list = list(self.cache_data.keys())
                index = keys_list.index(key)
                self.freq[index] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    min_key = min(self.freq, key=self.freq.get)
                    min_value = self.freq[min_key]
                    del_key = list(self.cache_data.keys())[min_key]
                    
                    keys_min_value = [key for key, value in self.freq.items() if value == min_value]
                    if len(keys_min_value) > 1:
                        inx_list = [self.order[key] for key in keys_min_value]
                        min_index = min(inx_list)
                        keys_list = list(self.cache_data.keys())
                        index_key = keys_list.index(min_index)
                        self.order.remove(min_index)
                        self.cache_data.pop(min_index)
                        print(f"DISCARD: {min_index}")
                    else:
                        self.cache_data.pop(del_key)
                        print(f"DISCARD: {del_key}")

                self.cache_data[key] = item
                self.order.append(key)
                keys_list = list(self.cache_data.keys())
                index = keys_list.index(key)
                self.freq[index] += 1

    def get(self, key):
        """
        Must return the value
        in self.cache_data linked to key.
        """
        if key is not None:
            if self.cache_data.get(key, None) is not None:
                self.order.remove(key)
                self.order.append(key)
                keys_list = list(self.cache_data.keys())
                index = keys_list.index(key)
                self.freq[index] += 1
                return self.cache_data.get(key, None)
        else:
            return None
