#!/usr/bin/python3
""" Module contains function to return dict description """


def class_to_json(obj):
    """ Returns dict description with simple data structure """
    return vars(obj)
