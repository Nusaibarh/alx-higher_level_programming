#!/usr/bin/python3
"""
This is an addition module to learn test cases
the function must add two integers and return reslt
the function works only on integer and floats
the function takes two arguements
this is all i can say about the function
"""


def add_integer(a, b=98):
    """
    This fucntion adds numbers
    The function adds 98 without second args
    The fucntion is perfect
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(a) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
