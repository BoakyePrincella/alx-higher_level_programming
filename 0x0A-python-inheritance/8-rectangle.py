#!/usr/bin/python3
"""The inheritance module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class inherits from the BaseGeometry class"""
    def __init__(self, width, height):
        """The instantiation function"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height
