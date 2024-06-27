#!/usr/bin/env python3
"""
"""
from base_caching import BaseCaching


def BasicCache(BaseCaching):
    """
    Object that allows storing and retirieving items
    from a dictionary
    """
    def put(self, key, item):
        """
        Adds an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item by key
        """
        return self.cache_data.get(key, None)
