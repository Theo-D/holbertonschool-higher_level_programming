#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = {}
    for pair in a_dictionary:
        newDict[pair] = a_dictionary[pair] * 2
    return newDict
