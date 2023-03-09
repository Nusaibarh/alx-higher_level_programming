#!/usr/bin/python3
"""
This is a square module
It is a lot easier to program with vscode
I am just going to increase comment
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    This is a square class inheriting a rextangle class
    This is a square class inheriting a rextangle class
    This is a square class inheriting a rextangle class
    This is a square class inheriting a rextangle class
    This is a square class inheriting a rextangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This is the constructor here...
        nothing special just using super class
        Comment
        """
        super(Square, self).__init__(size, size, x, y, id)

    def __repr__(self):
        """
        Overider represent of string
        Has a comment too
        """
        tt = self.id
        ty = super().x
        tr = super().y
        te = super().width
        return ("[Square] ({}) {}/{} - {}".format(tt, ty, tr, te))

    @property
    def size(self):
        """
        retrieve the width of rectangle
        """
        return (super().width)

    @size.setter
    def size(self, value):
        """
        This is where we give a new width
        """
        Rectangle.validator("width", value)
        Rectangle.width = value
        Rectangle.height = value

    @property
    def x(self):
        """
        This returns x value
        """
        return (super().x)

    @x.setter
    def x(self, value):
        """"
        sets the value of x
        """
        super().validatepos("x", value)
        super().x = value

    @property
    def y(self):
        """
        gets the value of y -vertical
        """
        return (super().y)

    @y.setter
    def y(self, value):
        """
        sets the value of y
        """
        super().validatepos("y", value)
        super().y = value

    def update(self, *args, **kwargs):
        """
        Will you believe i forgot to document this shit sha
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) > 1:
            Rectangle.width = args[1]
            Rectangle.height = args[1]
        if len(args) > 2:
            Rectangle.x = args[2]
        if len(args) > 3:
            Rectangle.y = args[3]
        if kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                Rectangle.width = kwargs['size']
                Rectangle.height = kwargs['size']
            if 'x' in kwargs:
                Rectangle.x = kwargs['x']
            if 'y' in kwargs:
                Rectangle.y = kwargs['y']

    def to_dictionary(self):
        """
        square to dictionary
        """
        dict = self.__dict__
        dict = {
                    "id": self.id,
                    "size": super().width,
                    "x": super().x,
                    "y": super().y
        }
        return (dict)
