#!/usr/bin/python3
"""
Module: 1-my_list
Class that inherets
from 'list'
"""


class MyList(list):
    """
    Class for organizing
    lists.

    Arguments:
        - list: Class List
    Attributes:
    ====================
    Public Instance Method:
        - def print_sorted(self)
    """

    def print_sorted(self):
        """
        Prints our list in
        ascending order
        """
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
