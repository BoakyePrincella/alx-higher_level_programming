#!/usr/bin/python3
"""The JSON representation"""


import json


def to_json_string(my_obj):
    """Json string representation"""
    if my_obj is None:
        return
    return json.dumps(my_obj)
