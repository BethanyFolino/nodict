#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Bethany Folino'


class Node:
    def __init__(self, key, value=None):
        self.hash = hash
        self.key = key
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.key}, {self.value})"

    def __eq__(self, other):
        # Your code here
        return


class NoDict:
    def __init__(self, num_buckets=10):
        self.buckets = None
        # Your code here

    def __repr__(self, key, value=None):
        # Your code here
        return

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
