#!/usr/bin/python3

""" this modules flips operators """


class MyInt(int):
    """Class to perform these operations"""
    def __eq__(self, other):
        """ Invert equality """
        return not super().__eq__(other)

    def __ne__(self, other):
        """Invert Inequality"""
        return not super().__ne__(other)
