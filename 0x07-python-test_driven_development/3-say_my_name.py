#!/usr/bin/python3
""" Module that prints a sentence with two strings as names """


def say_my_name(first_name, last_name=""):
    """Function that prints a sentence and two strings as names
        Prints white space if no second argument is given
        Raises TypeError if one of the arguments is not a string
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
