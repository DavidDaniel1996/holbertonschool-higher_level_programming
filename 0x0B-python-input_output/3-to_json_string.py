#!/usr/bin/python3
""" Module contains function to return JSON representation """


import json


def to_json_string(my_obj):
    """ Returns JSON representation of a string """
    json_rep = json.dumps(my_obj)
    return json_rep
