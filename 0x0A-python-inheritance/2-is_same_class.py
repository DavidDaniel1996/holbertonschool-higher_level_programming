#!/usr/bin/pyhton3
""" Module contains function to verify instance """


def is_same_class(obj, a_class):
    """ Verifies exact instance of object """
    if type(obj) in [a_class]:
        return True
    else:
        return False
