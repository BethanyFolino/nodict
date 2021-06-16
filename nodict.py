#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Bethany Folino with help from Jacob Short'
references = """https://www.pythontutorial.net/python-oop/python-__eq__/#:~:text=
               Python%20automatically%20calls%20the%20__,
               the%20__eq__%20method.
               https://stackoverflow.com/questions/12791501/python-
               initializing-a-list-of-lists"""


class Node:
    def __init__(self, key, value=None):
        self.hash = hash(key)
        self.key = key
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.key}, {self.value})"

    def __eq__(self, other):
        return self.key == other.key


class NoDict:

    def __init__(self, num_buckets=10):
        buckets = [[] for _ in range(num_buckets)]
        self.num_buckets = num_buckets
        self.buckets = buckets

    def __repr__(self):
        return "\n".join([f'{self.__class__.__name__}.{i}:{bucket}' for i,
                         bucket in enumerate(self.buckets)])

    def add(self, key, value):
        new_node = Node(key, value)
        index = new_node.hash % self.num_buckets
        for bucket_node in self.buckets[index]:
            if bucket_node == new_node:
                self.buckets[index].remove(bucket_node)
        self.buckets[index].append(new_node)

    def get(self, key):
        node_to_find = Node(key)
        index = node_to_find.hash % self.num_buckets
        for node_holder in self.buckets[index]:
            if node_holder == node_to_find:
                return node_to_find.value
        raise KeyError(f"{key} not found")

    def __getitem__(self, key):
        # Your code here
        return

    def __setitem__(self, key, value):
        # Your code here
        return
