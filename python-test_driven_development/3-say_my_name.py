#!/usr/bin/python3

"""
3-say_my_name
Contains a function that prints "My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if len(first_name) == 0:
        raise ValueError("first_name cannot be empty")

    print(f"My name is {first_name} {last_name}".strip())
