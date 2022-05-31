#!/usr/bin/python3
""" Module contains subclass Square """


rect = __import__('9-rectangle').Rectangle


class Square(rect):
    """ subclass Square, of subclass Rectangle """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
