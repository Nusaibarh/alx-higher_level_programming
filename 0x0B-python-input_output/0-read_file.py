#!/usr/bin/python3
"""
This module describe writinng to a file
method or function
what is goin on
modules up to
just about five lines
"""


def read_file(filename=""):
    """
    This function reads the content of a file
    and prints to stdoutput
    here
    """
    with open(filename, encoding="UTF8") as file:
        print(file.read(), end='')
