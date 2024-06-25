#!/usr/bin/env python3
"""
index_range return a tuple of size two containing a start and an end index
"""
from typing import Tuple


def index_range(page: int, page_size: int):
    """
    doc doc method
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
