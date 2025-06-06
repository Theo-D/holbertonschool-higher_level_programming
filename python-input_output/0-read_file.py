#!/usr/bin/python3
"""
0-read_file.py - Module containing method for reading file
"""


def read_file(filename=""):
    """
    Method for reading file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
