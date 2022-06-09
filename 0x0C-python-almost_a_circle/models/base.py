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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns json representation of a dictionary """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves json representation of a list of objects to a file """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ returns list of json string """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns instance with all attributes set """
        if cls.__name__ == "Rectangle":
            Dummy = cls(1, 1)
        else:
            Dummy = cls(1)
        Dummy.update(**dictionary)
        return Dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as jsonfile:
                read_data = jsonfile.read()
                json_rep = cls.from_json_string(read_data)
                list_instances = [cls.create(**o) for o in json_rep]
                return list_instances
        except FileNotFoundError:
            return "[]"
