#!/usr/bin/python3
"""A student class"""


class Student():
    """A student class"""
    def __init__(self, first_name, last_name, age):
        """Init instantiation function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This function converts a class to a json string"""
        if attrs is None:
            attrs = self.__dict__.keys()
        jsonrepr = {k: v for k, v in self.__dict__.items(
                ) if  k in attrs}
        return (jsonrepr)

    def reload_from_json(self, json):
        """Replaces all attributes wuth json attribute"""
        for k, v in json.items():
            setattr(self, k, v)
