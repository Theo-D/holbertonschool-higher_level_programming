#!/usr/bin/python
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
