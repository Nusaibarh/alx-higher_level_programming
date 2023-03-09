#!/usr/bin/python3
"""
The module reads from json file
"""


json = __import__("json")


def load_from_json_file(filename):
    """
    We load from json file
    """
    with open(filename, 'r', encoding="UTF-8") as file:
        obj = json.load(file)
    return (obj)
