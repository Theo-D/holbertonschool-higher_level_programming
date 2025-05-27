#!/usr/bin/python3
"""
Module containing definition for a class that represents a rectangle
and inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class representing a Rectangle
    """
    def __init__(self, width, height):
        """
        Object constructor for Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """
        Special method enforcing printing format for printing Rectangle
        """
        toPrint = "[{}] {}/{}".format(self.__class__.__name__, self.__width,
                                      self.__height)
        return toPrint

    def area(self):
        """
        Method calculating area of a Rectangle

        Returns area of a Rectangle
        """
        return self.__width * self.__height
