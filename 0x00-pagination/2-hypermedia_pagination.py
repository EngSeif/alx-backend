#!/usr/bin/env python3
"""
Simple helper function
"""

import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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
        """
        a method named get_page that takes two integer arguments page
        with default value 1 and page_size with default value 10.
        Use index_range to find the correct indexes to paginate the dataset
        correctly and return the appropriate page of the dataset
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        start, end = index_range(page, page_size)

        if start >= len(self.dataset()):
            return []
        elif end >= len(self.dataset()):
            end = len(self.dataset())

        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Implement a get_hyper method that takes the same arguments
        (and defaults) as get_page and returns a dictionary
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        data_dict = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
        return data_dict
