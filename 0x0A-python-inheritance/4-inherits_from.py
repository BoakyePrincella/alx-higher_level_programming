#!/usr/bin/python3
"""This is inherit_from module"""


def inherits_from(obj, a_class):
    """Returns True if inherited directly or indirectly"""
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
