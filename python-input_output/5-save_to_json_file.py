#!/usr/bin/python3
"""
5-save_to_json_file.py - Module containing function for serializing
python object to python file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function for serializing an object from a python
    """
    with open(filename, 'w', encoding="utf-8") as f:
        toWrite = f.write(json.dumps(my_obj))
    return toWrite
