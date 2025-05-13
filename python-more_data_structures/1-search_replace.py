#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = []
    for elm in my_list:
        if elm == search:
            newList.append(replace)
        else:
            newList.append(elm)
    return newList
