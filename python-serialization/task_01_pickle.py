#!/usr/bin/python3
"""
task_01_pickle.py - Module containing class describing a CustomObject.
"""
import pickle


class CustomObject:
    """
    Class for defining a custom object.
    """
    def __init__(self, name=None, age=None, is_student=None):
        """
        Object constructor for CustomObject
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Method for printing object's attributes
        in the right format
        """
        print("Name: {}\n".format(self.name),
              "Age: {}\n".format(self.age),
              "Is Student: {}\n".format(self.is_student))

    def serialize(self, filename):
        """
        Method for serailizing class attributes to file
        """
        with open(filename, 'wb') as f:
            pickle.dump(self.__dict__, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Class method for creating an object from a filename
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
        except FileNotFoundError:
            return None
        except EOFError:
            return None
        else:
            return cls(**obj)
