#!/usr/bin/python3

"""
Module containing definition of a class representing a Rectangle
"""


class Rectangle:
    """
    A class representing a rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0, print_symbol='#'):
        """
        Class constructor for a Rectangle object
        Args:
            width (int): Width of Rectangle.
            height (int): Height of Rectangle.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = print_symbol

    def __str__(self):
        """
        Prints a rectangle according to its height and width
        """
        rectStr = ""
        if self.__width == 0 or self.__height == 0:
            return rectStr
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    rectStr += str(self.print_symbol)
                if i != self.height - 1:
                    rectStr += '\n'
            return rectStr

    def __repr__(self):
        """
        Method for allowing eval instance method to instanciate
        a new rectangle object by using repr as arg

        Returns string in the right format
        """
        reprStr = "{}({}, {})".format(self.__class__.__name__,
                                      self.__width, self.__height)
        return reprStr

    def __del__(self):
        """
        Prints "Bye rectangle..." when del command is called on a Rectangle
        object
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @property
    def print_symbol(self):
        return self.__print_symbol

    @print_symbol.setter
    def print_symbol(self, print_symbol):
        self.__print_symbol = print_symbol

    def area(self):
        """
        Method returning area of a Rectangle

        Returns:
            result of width * height
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Method returning perimeter of a Rectangle

        Returns:
            result of (width * 2) + (height * 2)
        """
        return (self.__width * 2) + (self.__height * 2)
