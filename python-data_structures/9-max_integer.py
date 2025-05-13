#!/usr/bin/python3
def max_integer(my_list=[]):
    i = 0
    if len(my_list) == 0:
        return None
    for num in my_list:
        if num > i:
            i = num
    return i
