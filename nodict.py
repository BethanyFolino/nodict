#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Bethany Folino with help from Jacob Short and Matt Perry'
references = """https://www.pythontutorial.net/python-oop/python-__eq__/#:~:text=
               Python%20automatically%20calls%20the%20__,
               the%20__eq__%20method.
               https://stackoverflow.com/questions/12791501/python-
               initializing-a-list-of-lists"""


class Node:
    def __init__(self, key, value=None):
        """
        This method initializes key, value, and hash
        """
        self.hash = hash(key)
        self.key = key
        self.value = value

    def __repr__(self):
        """
        This method makes outputs be readable by humans
        """
        return f"{self.__class__.__name__}({self.key}, {self.value})"

    def __eq__(self, other):
        """
        This method compares keys to check to see if they are the same
        """
        return self.key == other.key


class NoDict:

    def __init__(self, num_buckets=10):
        """
        This method initializes num_buckets and a list of lists called
        buckets
        """
        buckets = [[] for _ in range(num_buckets)]
        self.num_buckets = num_buckets
        self.buckets = buckets

    def __repr__(self):
        """
        This method makes outputs legible to human eyes
        """
        return "\n".join([f'{self.__class__.__name__}.{i}:{bucket}' for i,
                         bucket in enumerate(self.buckets)])

    def add(self, key, value):
        """
        This makes an index by using hash of each Node with modulo and
        num_buckets, then compares current Node to Nodes in bucket_node,
        then removes the original if it finds a match or just adds it if not
        """
        new_node = Node(key, value)
        index = new_node.hash % self.num_buckets
        for bucket_node in self.buckets[index]:
            if bucket_node == new_node:
                self.buckets[index].remove(bucket_node)
        self.buckets[index].append(new_node)

    def get(self, key):
        """
        This uses hash to make an index like in add, but uses it to find
        the key of a matching node and return the corresponding value
        """
        node_to_find = Node(key)
        index = node_to_find.hash % self.num_buckets
        for node_holder in self.buckets[index]:
            if node_holder == node_to_find:
                return node_holder.value
        raise KeyError(f"{key} not found")

    def __getitem__(self, key):
        """
        This magic method allows square brackets to be used for
        assignment by calling the get method that was made above
        """
        return self.get(key)

    def __setitem__(self, key, value):
        """
        This magic method allows square bracket assigned items to be
        read properly by calling the previously created add method
        """
        self.add(key, value)
