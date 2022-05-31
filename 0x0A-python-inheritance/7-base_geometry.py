#!/usr/bin/python3
""" Module contains class BaseGeometry """


class BaseGeometry:
    """ Defines class BaseGeometry """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) not in [int]:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
