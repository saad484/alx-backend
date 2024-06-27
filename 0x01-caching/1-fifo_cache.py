#!/usr/bin/env python3
"""
DOC DOC Object
"""
from base_caching import BaseCaching
from collections import OrderedDict


def FIFOCache(BaseCaching):
    """
    Rerpresents an Object that allows storing and retrieving items
    from a dictionary with a FIFO removal mechanism when the limit is
    reached
    """
    def __init__(self):
        """
        Initializes the cache
        """
        super.cache_data() = OrderedDict()

    def put(self, key, item):
        """
        Adds an item in the cache
        """
        if the key is None or items is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print('DISCARD:', first_key)

    def get(self, key):
        """
        retrieves an item by key
        """
        return self.cache_data.get(key, None)
