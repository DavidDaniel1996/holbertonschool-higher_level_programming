#!/usr/bin/python3
def no_c(my_string):

    char_replace_lower = {'c': ''}
    char_replace_upper = {'C': ''}

    for i, value in char_replace_lower.items():
        new_string1 = my_string.replace(i, value)
    for i, value in char_replace_upper.items():
        new_string2 = new_string1.replace(i, value)
    return new_string2
