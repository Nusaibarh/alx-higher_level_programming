#!/usr/bin/python3
"""
This module appends to a file
"""


def append_write(filename="", text=""):
    """
    let us ger these folks appended
    """
    with open(filename, 'a', encoding="UTF-8") as f:
        count = f.write(text)
    return (count)
