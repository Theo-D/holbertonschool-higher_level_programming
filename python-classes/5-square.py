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

    @property
    def size(self):
        """
        Gets value of size

        Sets value of size enforcing type (integer) and value (>= 0)
        """
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Method returning area of a Square

        Returns:
            result of size * size
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints a square of height "size" and width "size"
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
