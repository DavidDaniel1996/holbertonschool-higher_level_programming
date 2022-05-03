#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        idx = 0
        my_list.reverse()
        for i in range(len(my_list)):
            print(my_list[idx])
            idx += 1
