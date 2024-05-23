#!/usr/bin/python3
"""Python input and output"""


def read_file(filename=""):
    """Read the python file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
