#!/usr/bin/python3
"""
3-to_json_string.py - Module containing method for serializing data
"""
import json


def to_json_string(my_obj):
    """
    Method returning serialized data
    """
    return json.dumps(my_obj)
