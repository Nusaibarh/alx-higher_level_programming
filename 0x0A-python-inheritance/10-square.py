#!/usr/bin/python3
"""
This is whatvi do with my night
I believe it pays off for me
This is a module with inherited class
Rectangle is inherited daga geometry
geomerty ya na daga object
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    We have inherited Geomentry into Rectangle
    Now we wirte cerrain methods for rectangle
    """

    def __init__(self, size):
        """
        We initialize rectangle
        we validate the width
        likewise the length
        """
        Rectangle.integer_validator(self, "size", size)
        self._Square__size = size

    def area(self):
        """
        computes the area of the rectangle
        for those who do not know the formulae
        it is the product of width and height
        """
        return (self._Square__size ** 2)

    def __str__(self):
        """
        This prints the class and info about it
        The info ks what we have receive which cannor
        be changed
        """
        pp = str(self._Square__size) + "/" + str(self._Square__size)
        return ("[Rectangle] " + pp)
