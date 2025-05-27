#!/usr/bin/python3
"""
Module containing definition for inhertis_from
"""
def inherits_from(obj, a_class):
    """
    Checks if obj inherits of the class a_class

    Returns True if inherits, otherwise returns False
    """
    return issubclass(obj, a_class)
