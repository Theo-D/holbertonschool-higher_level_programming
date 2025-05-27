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
        Method calculating area of a Rectangle

        Returns area of a Rectangle
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validates a value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
