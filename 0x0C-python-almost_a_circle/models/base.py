#!/usr/bin/python3
""" Module contains Base class """


class Base():
    """ base class """
    __nb_objects = 0


    def __init__(self, id=None):
        """ class constructor """
        if id != None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
