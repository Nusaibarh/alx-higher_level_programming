#!/usr/bin/python3
"""
Oh my God....My class is gotta creste a json representation
of itsself... lets get the method in
"""


class Student:
    """
    This guy is our test example
    """

    def __init__(self, first_name, last_name, age):
        """
        initializer method to get some stuffs
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        convert to dictrionary... now
        """
        if type(attrs) is not list:
            return (vars(self))
        all_dict = vars(self)
        f_dict = {}
        for i in range(len(attrs)):
            if attrs[i] in all_dict:
                key = attrs[i]
                key_value = {key: all_dict[key]}
                f_dict.update(key_value)
        return (f_dict)
