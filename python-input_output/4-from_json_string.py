#!/usr/bin/python3
"""
4-from_json_string.py - Module containing method for deserializing data
"""
import json


def from_json_string(my_str):
    """
    Method for deserializing data
    """
    return json.loads(my_str)
