#!/usr/bin/python3
"""
6-load_from_json_file.py - Module containing method for deserializing
from file
"""
import json


def load_from_json_file(filename):
    """
    Method for deserializing from json file.
    Return: a python object containing deserialized data
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.loads(f.read())
