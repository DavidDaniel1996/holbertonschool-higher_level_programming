#!/usr/bin/pyhton3
def is_same_class(obj, a_class):
    """ Verifies instance of object """
    if type(obj) in [a_class]:
        return True
    else:
        return False
