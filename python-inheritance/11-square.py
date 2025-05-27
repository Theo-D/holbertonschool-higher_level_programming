#!/usr/bin/python3
"""
Module containing definition for a class that represents a Square
and inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class representing a Square
    """
    def __init__(self, size):
        """
        Object constructor for Square
        """
        self.integer_validator("Size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Special method enforcing printing format for printing Rectangle
        """
        toPrint = "[{}] {}/{}".format(self.__class__.__name__, self.__width,
                                      self.__height)

    def area(self):
        """
        Method calculating area of a Square

        Returns area of a Square
        """
        return self.__size * self.__size
