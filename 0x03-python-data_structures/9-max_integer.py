#!/usr/bin/python3
def max_integer(my_list=[]):
    num = 0
    idx = 0
    if len(my_list) == 0:
        return None
    else:
        for i in range(len(my_list)):
            if num < my_list[idx]:
                num = my_list[idx]
            idx += 1
        return num
