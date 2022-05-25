#!/usr/bin/python3
""" Module contains class Rectangle """


class Rectangle:
    """ Define Rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0:
            return 0
        elif self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.height == 0:
            return ""
        if self.width == 0:
            return ""
        my_list = []
        for i in range(self.height):
            my_list.append(str(self.print_symbol) * self.width)
            if i != self.height - 1:
                my_list.append('\n')

        return "".join(my_list)

    def __repr__(self):
        rep = 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'
        return rep

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
