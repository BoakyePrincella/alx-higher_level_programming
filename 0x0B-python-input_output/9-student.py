#!/usr/bin/python3
"""A student class"""


class Student():
    """A student class"""
    def __init__(self, first_name, last_name, age):
        """Init instantiation function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(obj):
        """This function converts a class to a json string"""
        jsonrepr = {j: v for j, v in obj.__dict__.items(
                ) if not j.startswith("__")}
        return (jsonrepr)
