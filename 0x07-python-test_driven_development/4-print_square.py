#!/usr/bin/python3
""" Module that prints a square the size of size """


def print_square(size):
    """Function that prints a square with #
        Raises TypeError if size is not an integer
        Raises ValueError if size is less than 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
