#!/usr/bin/python3
def best_score(a_dictionary):
    i = 0
    if a_dictionary is None:
        return None
    for pair in a_dictionary:
        if a_dictionary[pair] > i:
            i = a_dictionary[pair]
            res = pair
    return res
