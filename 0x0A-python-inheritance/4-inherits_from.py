#!/usr/bin/python3
"""
In this module
we want to check
for base class
in a sub class
hope you get the point now
"""


def inherits_from(obj, a_class):
    """
    This does not only check for class
    it also check for base too
    implenting...
    """
    return (issubclass(type(obj), a_class))
