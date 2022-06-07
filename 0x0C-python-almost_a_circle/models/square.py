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
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
