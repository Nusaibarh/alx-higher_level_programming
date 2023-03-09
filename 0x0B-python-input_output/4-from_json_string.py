#!/usr/bin/python3
"""
This module decodes a jason
"""


json = __import__("json")


def from_json_string(my_str):
    """
    json back to an object
    """
    obj = json.loads(my_str)
    return (obj)
