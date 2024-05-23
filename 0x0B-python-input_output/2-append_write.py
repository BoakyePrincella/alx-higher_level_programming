#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """The append_write method"""
    if filename is None or type(filename) is not str:
        return
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
