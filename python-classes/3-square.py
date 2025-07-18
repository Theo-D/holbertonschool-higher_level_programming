#!/usr/bin/python3

"""
Module containing definition of a class representing a Square
"""


class Square:
    """
    class representing a square
    """
    def __init__(self, size=0):
        """
        Class constructor for a Square object
        Args:
            size (int): Height and Width of Square
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Method returning area of a Square
        """
        return self.__size * self.__size
