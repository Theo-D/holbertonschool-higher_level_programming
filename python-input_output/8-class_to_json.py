#!/usr/bin/python3
"""
8-class_to_json.py - Module for serializing class
"""


def class_to_json(obj):
    """
    Method for serializing an object
    """
    return obj.__dict__
