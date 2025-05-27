#!/usr/bin/python3
"""
A module for training abstract methods and duck typing.
"""
from abc import ABC, abstractmethod
from math import pi



class Shape(ABC):
    """
    A class representing an abstract Shape.
    """
    @abstractmethod
    def area(self):
        """
        Method returning the area of a Shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Method returning the area of a Shape.
        """
        pass

class Circle(Shape):
    """
    A class representing a Circle.
    """
    def __init__(self, radius):
        """
        Object constructor for the class Circle
        """
        self.__radius = abs(radius)

    def area(self):
        """
        Method returning area of a Circle.
        """
        return pi * (self.__radius ** 2)

    def perimeter(self):
        """
        Method returning perimeter of a Circle
        """
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """
    A class representing a Rectangle.
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        """
        Method returning area of a Rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Method returning perimeter of a Rectangle.
        """
        return 2 * (self.__width + self.__height)

def shape_info(shapeObj):
    """
    Methods printing area and perimeter of given object according
    to their respective method definition.
    """
    print("Area: {}".format(shapeObj.area()))
    print("Perimeter: {}".format(shapeObj.perimeter()))
