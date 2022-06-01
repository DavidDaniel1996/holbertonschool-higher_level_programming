#!/usr/bin/python3
""" Module contains function to return to object """


import json


def from_json_string(my_str):
    """ Returns object from JSON representation """
    decoded = json.loads(my_str)
    return decoded
