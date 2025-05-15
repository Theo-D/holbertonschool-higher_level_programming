#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    newList = my_list[::-1]
    for i in newList:
        print("{:d}".format(i))
