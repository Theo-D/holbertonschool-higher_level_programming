#!/usr/bin/python3
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
        self.__width = width
        self.__height = height

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
                    rectStr += '#'
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
