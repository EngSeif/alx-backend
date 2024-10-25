#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        method with two integer arguments:
        index with a None default value and page_size
        with default value of 10.
        The method should return a dictionary
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        assert index > -1
        assert index < total_pages - 1

        results = []
        current_index = index

        while len(results) < page_size:
            if current_index in self.__indexed_dataset:
                value = self.__indexed_dataset[current_index]
                if value is not None:
                    results.append(value)
            current_index += 1
        data_dict = {
            'index': index,
            'next_index': current_index,
            'page_size': page_size,
            'data': results
            }
        return data_dict
