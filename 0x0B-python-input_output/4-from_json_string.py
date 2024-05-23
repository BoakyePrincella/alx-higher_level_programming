#!/usr/bin/python3
"""The JSON representation"""


import json


def from_json_string(my_str):
    """Object representation"""
    if my_str is None:
        return
    return json.loads(my_str)
