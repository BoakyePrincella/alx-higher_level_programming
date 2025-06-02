#!/usr/bin/python3
""" Creating a square class """


class Square:
    """ Defining a class square """
    def __init__(self, size=0):
        """ Initializing a square class
        Args: size=0: size of the square
         """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ Initialising a property attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """ Iniatialising a setter """
        self.__size = value

    def area(self):
        """ Calculating the area of the square """
        return self.__size ** 2
