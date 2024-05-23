#!/usr/bin/python3
"""This is an inheritance module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The square class inheriting from Rectangle class"""
    def __init__(self, size):
        """The instatiantion function"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self._size = size

    def area(self):
        """The area method"""
        return (self._size ** 2)
