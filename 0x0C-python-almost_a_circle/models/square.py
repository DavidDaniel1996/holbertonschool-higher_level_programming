#!/usr/bin/python3
""" Module contains Square Class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Define Square, subclass of Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = self.width

    def __str__(self):
        """ Defines str for Square """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__width}"

    @property
    def size(self):
        """ size getter """
        return self.__width

    @size.setter
    def size(self, value):
        """ size setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def update(self, *args, **kwargs):
        """ Adds update functionality """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            values = args
            for i in range(len(args)):
                setattr(self, attributes[i], values[i])
        else:
            attributes = ['id', 'size', 'x', 'y']
            for attributes in kwargs:
                setattr(self, attributes, kwargs[attributes])

    def to_dictionary(self):
        """ returns dictionary representation """
        pd1 = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return pd1