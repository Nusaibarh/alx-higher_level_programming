#!/usr/bin/python3
"""
This is a module
It is a base geometry one
For now it is empty
stay tuned while we work on filling it up
oh yeah
this is enough
"""


class BaseGeometry(object):
    """
    This is a class inherited from object
    This is empty now
    pass for now while we create
    """
    pass

    def __init__(self):
        """
        Nothing is to be here
        """
        pass

    def area(self):
        """
        How can we find area without length and breadth
        we do not know the shape either
        this method is waiting for init
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates that our input is integer
        name is assumed to be always string
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
