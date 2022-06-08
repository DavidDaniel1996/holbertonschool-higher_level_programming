#!/usr/bin/python3
""" Module contains Base class """

import json


class Base():
    """ base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ returns json representation of a dictionary """
        if list_dictionaries is None:
            return "[]"
        dict_rep = json.dumps(list_dictionaries)
        return dict_rep
