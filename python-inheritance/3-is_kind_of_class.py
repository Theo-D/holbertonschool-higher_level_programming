#!/usr/bin/python3
"""
Module containing definition for is_kind_of_class
"""
def is_kind_of_class(obj, a_class):
    """
    Checks if obj is as instance of the class a_class

    Returns True if is instance, otherwise returns False
    """
    return isinstance(obj, a_class)
