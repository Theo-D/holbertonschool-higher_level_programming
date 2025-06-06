#!/usr/bin/python3
"""
11-sutdent.py - Module containing a class describing a student
"""


class Student:
    """
    A class representing a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Object constructor for Student
        args:
            first_name: Strudent's first name
            last_name: student's last name
            age: student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Method to serialize student's attributes.
        return a dictionary of attributes.
        """
        newDict = {}
        if isinstance(attrs, list) and all(isinstance(elm, str)
                                           for elm in attrs):
            for elm in attrs:
                if elm in self.__dict__.keys():
                    newDict.update({elm: self.__dict__[elm]})
            return newDict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Method for setting student's attributes from json file.
        """
        for key in json:
            if key in self.__dict__.keys():
                setattr(self, key, json[key])
