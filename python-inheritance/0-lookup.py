#!/usr/bin/python3
"""
This module contains a function for returning methods and attributes
of a given object.
"""
def lookup(obj):
    """
    A function that returns attributes and methods of a given object.
    Returns a list of said attributes and methods
    """
    return dir(obj)
