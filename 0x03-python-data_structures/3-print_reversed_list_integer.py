#!/usr/bin/python3
from re import M


def print_reversed_list_integer(my_list=[]):
    idx = -1
    for i in range(len(my_list)):
        print(my_list[idx])
        idx -= 1
