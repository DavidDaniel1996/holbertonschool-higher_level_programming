#!/usr/bin/python3
""" Module contains class MyList, inherets list """


class MyList(list):
    """ Defines MyList """
    def print_sorted(self):
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
