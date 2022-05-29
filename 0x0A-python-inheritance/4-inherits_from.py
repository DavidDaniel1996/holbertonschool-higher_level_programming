#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ Check if obj is sub class of a_class """
    result = issubclass(type(obj), a_class)
    if result is True:
        if type(obj) == a_class:
            return False
    return result
