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
