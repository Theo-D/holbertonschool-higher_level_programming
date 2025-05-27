#!/usr/bin/python3

"""
7-base_geometry
A module containing the definition of a class deifining base geometry
"""


class BaseGeometry:
    """
    Class defining comcepts of base geometry
    """
    def area(self):
        """
        Method only raising an excepttion for now
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validates a value
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
