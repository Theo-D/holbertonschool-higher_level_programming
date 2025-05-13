#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    isKeyExist = False
    for pair in a_dictionary:
        if pair == key:
            a_dictionary[key] = value
            isKeyExist = True
    if not isKeyExist:
        a_dictionary[key] = value
    return a_dictionary
