#!/usr/bin/python
def divisible_by_2(my_list=[]):
    newList = []
    for num in my_list:
        if num % 2 == 0:
            newList.append(True)
        else:
            newList.append(False)
    return newList
