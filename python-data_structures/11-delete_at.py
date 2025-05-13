#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    i = 0
    newList = []
    for elm in my_list:
        if idx != i:
            newList.append(elm)
        i += 1
    return newList
