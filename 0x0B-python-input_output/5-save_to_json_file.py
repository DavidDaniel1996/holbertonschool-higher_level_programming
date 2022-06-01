#!/usr/bin/python3
""" Module containing write to file using json function """


import json


def save_to_json_file(my_obj, filename):
    """ Writes to a file using json representation """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
