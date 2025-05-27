#!/usr/bin/python3

"""
Module containing definition for is_same_class
"""


def is_same_class(obj, a_class):
    """
    Checks if obj is exactly and object of the class a_class

    Returns True if is object, otherwise returns False
    """
    return obj.__class__ is a_class
