#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = list(set(set_1).difference(set_2))
    set_3.extend(set(set_2).difference(set_1))
    return set_3
