#!/usr/bin/python3

"""
Module containing definition of a class representing a Square
"""


class Square:
    """
    class representing a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Class constructor for a Square object
        Args:
            size (int): Height and Width of Square
            position (int, int): Tuple of ints for x and y position of Square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Gets value of position.

        Sets position enforcing type (int, int) and tuple length (==2)
        """
        return self.__position

    @position.setter
    def position(self, value):
        for i in value:
            if not isinstance(i, int):
                isInt = False
            else:
                isInt = True
        if len(value) != 2 and isInt is True:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
        at "position" coordinates.
        """
        if self.__size == 0:
            print()
        else:
            if self.__position[0] > 0:
                print(f"{'\n' * self.__position[0]}", end="")
            for i in range(self.__size):
                if self.__position[1] > 0:
                    print(f"{'_' * self.__position[1]}", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
