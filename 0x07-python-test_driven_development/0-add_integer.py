#!/usr/bin/python3
""" Module to add two integers """


def add_integer(a, b=98):
    """Function to return sum of two integers
        If an argument is not an integer, raises TypeError 
    """

    try:
        a = int(a)
    except (ValueError, TypeError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (ValueError, TypeError):
        raise TypeError("b must be an integer")

    return a + b
