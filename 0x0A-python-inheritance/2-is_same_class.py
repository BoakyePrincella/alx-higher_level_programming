#!/usr/bin/python3
"""the is_same_class module """


def is_same_class(obj, a_class):
    """Returns True if obj is an instance of a_class"""
    return (type(obj) is a_class)
