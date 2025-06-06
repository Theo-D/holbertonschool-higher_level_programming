#!/usr/bin/python3
"""
2-append_write.py - Module containing method for appending text
to a file.
"""


def append_write(filename="", text=""):
    """
    Method for appending text to a file.
    Returns number of characters written
    """
    with open(filename, 'a', encoding="utf-8") as f:
        charCount = f.write(text)
    return charCount
