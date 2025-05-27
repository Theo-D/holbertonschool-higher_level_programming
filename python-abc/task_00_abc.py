#!/usr/bin/python3

"""
task_00_abc
Module for practicing with creating abstract classes and using duck typing
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    A class defining an abstraction of an animal
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method defining sound produced by ananimal
        """
        pass


class Dog(Animal):
    """
    A class representing a dog
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    A class representing a dog
    """
    def sound(self):
        return "Meow"
