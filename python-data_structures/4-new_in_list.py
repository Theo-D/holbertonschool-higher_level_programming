#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newList = my_list.copy()
    if idx < 0 or idx > len(newList) - 1:
        return newList
    else:
        newList[idx] = element
        return newList
