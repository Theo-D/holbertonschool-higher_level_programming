#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    newDict = dict(sorted(a_dictionary.items()))
    for pair in newDict:
        print("{}: {}".format(pair, newDict[pair]))
