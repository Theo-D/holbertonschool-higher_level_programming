#!/usr/bin/python3
"""
9 - student.py - Module containing a class describing a student
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

    def to_json(self):
        """
        Method to serialize student's attributes.
        return a dictionary of attributes.
        """
        return self.__dict__
