#!/usr/bin/python3
"""
We want to return the self init of a class as dictionary
"""


def class_to_json(obj):
    return (vars(obj))
