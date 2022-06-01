#!/usr/bin/python3
""" Module contains function to create object from json file """


import json


def load_from_json_file(filename):
    """ obtains json string from json file and converts it to object """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    decoded = json.loads(read_data)
    return decoded
