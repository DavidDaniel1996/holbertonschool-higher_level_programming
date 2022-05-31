#!/usr/bin/python3
""" Module contains function to verify instance and class """


def is_kind_of_class(obj, a_class):
    """ Verifies instance and class of object """
    result = isinstance(obj, a_class)
    return result
