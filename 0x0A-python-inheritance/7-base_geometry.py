#!/usr/bin/python3
"""The BaseGeometry class"""


class BaseGeometry():
    """The BeseGeometry class"""
    def area(self):
        """Return the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
