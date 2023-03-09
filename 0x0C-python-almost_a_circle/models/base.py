#!/usr/bin/python3
"""
This module is the contains a class
the class is the base of all modules
amd also classes
"""


import json


class Base(object):
    """
    all classes is based om this class for this project...
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is the initializer
        It gives ID  to all classes created from this module
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def validator(Name, value):
        """
        This is to save me lots of typing stress
        This validates all data inputed
        """
        if type(value) is not int:
            raise TypeError(Name + " must be an integer")
        if value < 1:
            raise ValueError(Name + " must be > 0")

    def validatepos(Name, value):
        """
        This one validates the position adjuster
        We need an integer not more less than zero"
        """
        if type(value) is not int:
            raise TypeError(Name + " must be an integer")
        if value < 0:
            raise ValueError(Name + " must be >= 0")

    @staticmethod
    def to_json_string(list_dictionaries):
        jstr = "["
        if list_dictionaries is None:
            jstr += "]"
            return (jstr)
        if len(list_dictionaries) == 0:
            jstr += "]"
            return (jstr)
        jstr = json.dumps(list_dictionaries)
        return (jstr)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Ready to convert object to file now
        """
        list_obj = []
        if list_objs is None:
            pass
        else:
            for inst in list_objs:
                list_obj.append(inst.to_dictionary())
        filepath = cls.__name__
        filepath += ".json"
        jsonstr = cls.to_json_string(list_obj)
        with open(filepath, "w") as file:
            file.write(jsonstr)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a string represeting a list of dictionaries
        to a real list
        """
        list = []
        if json_string is None:
            pass
        else:
            list = json.loads(json_string)
        return (list)
