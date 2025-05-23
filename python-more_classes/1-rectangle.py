#!/usr/bin/python3

"""
Module containing definition of a class representing a Rectangle
"""


class Rectangle:
    """
    A class representing a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Class constructor for a Rectangle object
        Args:
            width (int): Width of Rectangle.
            height (int): Height of Rectangle.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        elif height < 0:
            raise ValueError("width must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        Gets value of width

        Sets value of width enforcing type (integer) and value (>= 0)
        """
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """
        Gets value of height

        Sets value of height enforcing type (integer) and value (>= 0)
        """
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        elif height < 0:
            raise ValueError("width must be >= 0")
        self.__height = height
