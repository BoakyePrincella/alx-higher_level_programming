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

    def __str__(self):
        """The string representation"""
        return ("[Rectangle] {}/{}".format(self._width, self._height))

    def area(self):
        """The area function"""
        return self._width * self._height
