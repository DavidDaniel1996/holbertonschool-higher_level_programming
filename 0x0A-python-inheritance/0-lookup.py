#!/usr/bin/python3
""" Module for function that returns dict """


def lookup(obj):
    """ returns a list of attributes and methods """
    var = dir(obj)
    return var
