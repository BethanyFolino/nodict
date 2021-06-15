#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Bethany Folino'
references = """https://www.pythontutorial.net/python-oop/python-__eq__/#:~:text=
               Python%20automatically%20calls%20the%20__,
               the%20__eq__%20method.
               https://stackoverflow.com/questions/12791501/python-
               initializing-a-list-of-lists"""


class Node:
    def __init__(self, key, value=None):
        self.hash = self.__hash__
        self.key = key
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.key}, {self.value})"

    def __eq__(self, other):
        return self.key == other.key


class NoDict:

    def __init__(self, buckets=[], num_buckets=10):
        buckets = [[] for _ in range(num_buckets)]
        self.num_buckets = num_buckets
        self.buckets = buckets
        # Your code here

    def __repr__(self):
        # Your code here
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i,
                         bucket in enumerate(self.buckets)])

    def add(self, key, value):
        # Your code here
        return

    def get(self, key):
        # Your code here
        return

    def __getitem__(self, key):
        # Your code here
        return

    def __setitem__(self, key, value):
        # Your code here
        return
