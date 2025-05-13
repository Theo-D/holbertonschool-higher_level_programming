#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for list in matrix:
        newList = []
        for num in list:
            newList.append(num ** 2)
        newMatrix.append(newList)
    return newMatrix
