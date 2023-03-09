#!/usr/bin/python3
"""
This is whatvi do with my night
I believe it pays off for me
This is a module with inherited class
Rectangle is inherited daga geometry
geomerty ya na daga object
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    We have inherited Geomentry into Rectangle
    Now we wirte cerrain methods for rectangle
    """

    def __init__(self, width, height):
        """
        We initialize rectangle
        we validate the width
        likewise the length
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self._Rectangle__width = width
        self._Rectangle__height = height

    def area(self):
        """
        computes the area of the rectangle
        for those who do not know the formulae
        it is the product of width and height
        """
        return (self._Rectangle__width * self._Rectangle__height)

    def __str__(self):
        """
        This prints the class and info about it
        The info ks what we have receive which cannor
        be changed
        """
        pp = str(self._Rectangle__width) + "/" + str(self._Rectangle__height)
        return ("[Rectangle] " + pp)
