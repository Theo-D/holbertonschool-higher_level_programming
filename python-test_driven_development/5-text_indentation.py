#!/usr/bin/python3

"""
5-text_indentation
Contains a function that prints a text with 2 new lines after each of these
characters: . ? and :
"""


def text_indentation(text):
    sep = ['.', '?', ':']
    start = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i, char in enumerate(text):
        if char in sep:
            print("{}".format(text[start:i + 1]).strip())
            print()
            start = i + 1
    if start < len(text):
        print("{}".format(text[start:]).strip(), end="")
