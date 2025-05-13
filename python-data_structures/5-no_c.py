#!/bin/bash/python3
def no_c(my_string):
    newString = ""
    for letter in my_string:
        if ord(letter) != 67 and ord(letter) != 99:
            newString += letter
    return newString
