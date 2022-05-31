#!/usr/bin/python3
""" Module contains class BaseGeometry """


class BaseGeometry:
    """ Defines class BaseGeometry """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) not in [int]:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
