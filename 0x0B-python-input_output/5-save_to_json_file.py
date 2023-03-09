#!/usr/bin/python3
"""
Jason to be in file
"""


json = __import__("json")


def save_to_json_file(my_obj, filename):
    """
    saving to jsonfile not string
    """
    with open(filename, 'w', encoding="UTF-8") as file:
        json.dump(my_obj, file)
