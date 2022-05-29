#!/usr/bin/python3
""" Module contains subclass Square """


rect = __import__('9-rectangle').Rectangle


class Square(rect):
    """ subclass Square, of subclass Rectangle """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        rect.integer_validator(self, "size", self.__size)

    def area(self):
        result = self.__size * self.__size
        return result
