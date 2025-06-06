#!/usr/bin/python3
"""
1-write_file.py - Module containing method for writing text to a file
"""


def write_file(filename="", text=""):
    """
    Method for writing text to a file
    Returns count of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        charCount = f.write(text)
    return charCount
