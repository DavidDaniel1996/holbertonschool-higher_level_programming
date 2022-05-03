#!/usr/bin/python3
def no_c(my_string):

    char_replace_lower = {'c': ''}
    char_replace_upper = {'C': ''}

    new_string1 = my_string.translate(str.maketrans(char_replace_lower))
    new_string2 = new_string1.translate(str.maketrans(char_replace_upper))
    return new_string2
