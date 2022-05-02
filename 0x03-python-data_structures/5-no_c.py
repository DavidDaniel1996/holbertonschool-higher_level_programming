#!/usr/bin/python3
def no_c(my_string):
    idx = 0
    new_string = ""
    for i in range(len(my_string)):
        if my_string[idx] == "c" or my_string[idx] == "C":
            new_string = my_string[:idx] + my_string[idx + 1:]
        idx += 1
    return new_string
