#!/usr/bin/env python3
"""
Title: Simple helper function
Description: A function named index_range that takes two integer
arguments page and page_size
Author: @a_idk
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ fxn that takes two int args and returns a tuple of size two """

    start = (page - 1) * page_size  # minus 1 to account for index 0
    end = start + page_size

    return (start, end)
