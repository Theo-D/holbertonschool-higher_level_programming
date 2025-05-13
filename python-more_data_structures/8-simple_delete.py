#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    newDict = {}
    for pair in a_dictionary:
        if pair != key:
            newDict[pair] = a_dictionary[pair]
    if len(newDict) > 0:
        return newDict
    else:
        return a_dictionary
