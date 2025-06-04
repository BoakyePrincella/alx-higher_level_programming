#!/usr/bin/python3
"""This module adds new attribute"""


def add_attribute(obj, attr_name, value):
    """Function that add new attribute if possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, value)
