#!/usr/bin/env python3
"""
Title: Hypermedia pagination
Description: A function named index_range that takes two integer
arguments page and page_size
Author: @a_idk
"""

import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ fxn that takes two int args and returns a tuple of size two """

    start = (page - 1) * page_size  # minus 1 to account for index 0
    end = start + page_size

    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ fxn that retrieves page of data """

        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start > len(data):
            return []

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ method that takes args and returns a dictionary """

        """ data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)

        return {
                'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': page + 1 if end < len(self.__dataset) else None,
                'prev_page': page - 1 if start > 0 else None,
                'total_pages': total_pages
                }
        # return page_info
        """
        assert type(index) == int
        assert type(page_size) == int
        # Getting and Sizing the Indexed Dataset
        csv = self.indexed_dataset()
        csv_size = len(csv)

        assert 0 <= index < csv_size  # Checking the Validity of the Index

        data = []
        next_index = index

        for _ in range(page_size):
            while not csv.get(next_index):
                next_index += 1
                data.append(csv.get(next_index))
                next_index = next_index + 1

                return {
                        "index": index,
                        "data": data,
                        "page_size": page_size,
                        "next_index": next_index
                        }
