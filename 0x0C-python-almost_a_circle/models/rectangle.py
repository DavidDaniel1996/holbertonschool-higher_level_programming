#!/usr/bin/python3
""" Module contains Rectangle class """

from models.base import Base


class Rectangle(Base):
    """ Define Rectnangle, subclass of Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area functionality """
        return self.__height * self.__width

    def display(self):
        """ prints # based on width and height,
        and whitespace based on x and y
        """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """ returns attributes of rectangle in string format """
        s = "[Rectangle] ("
        return f"{s}{self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """ Adds update functionality """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            values = args
            for i in range(len(args)):
                setattr(self, attributes[i], values[i])
        else:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for attributes in kwargs:
                setattr(self, attributes, kwargs[attributes])

    def to_dictionary(self):
        """ returns dictionary representation """
        pd1 = {'x': self.x, 'y': self.y, 'id': self.id}
        pd2 = {'height': self.height, 'width': self.width}
        pd1.update(pd2)
        return pd1
