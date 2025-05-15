#!/usr/bin/python3
def no_c(my_string):
    newString = ""
    for letter in my_string:
        if letter != 'C' and letter != 'c':
            newString += letter
    return newString
