#!/usr/bin/python3
"""
12-pascal_triangle.py - Module containing a function for building
a pascal triangle
"""


def pascal_triangle(n):
    """
    Function for building a Pascal triangle
    return a list of list
    """
    newList = []
    if n <= 0:
        return newList
    for i in range(n):
        row = [1]
        for j in range(1, i):
            sum = newList[row - 1][i - 1] + newList[row - 1][i]
            row.append(sum)
            if row > 0:
                row.append(1)
                newList.append(row)
    return newList
