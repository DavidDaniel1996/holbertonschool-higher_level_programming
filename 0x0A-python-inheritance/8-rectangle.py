#!/usr/bin/python3
""" Module contains subclass Rectangle """


bg = __import__('7-base_geometry').BaseGeometry


class Rectangle(bg):
    """ subclass Rectangle, of class BaseGeometry """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        bg.integer_validator(self, "width", self.__width)
        bg.integer_validator(self, "height", self.__height)
