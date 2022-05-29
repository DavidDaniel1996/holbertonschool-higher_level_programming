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

    def area(self):
        result = self.__height * self.__width
        return result

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")
