#!/usr/bin/python3
"""
Module containing functions to serialize and deserialize data.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Function for serializing and saving data to a file.
    """
    str = json.dumps(data)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(str)


def load_and_deserialize(filename):
    """
    Function for deserializing data from a file.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        str = json.loads(f.read())

    return str
