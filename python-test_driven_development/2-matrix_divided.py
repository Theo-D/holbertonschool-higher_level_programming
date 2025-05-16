#!/usr/bin/python3


"""
1-matrix_divided
Contains a function divides all elements of a matrix.
Return: integer
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    """
    newMatrix = []
    rowLen = len(matrix[0])

    # Testing for div:
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Testing for matrix and it content:
    if not isinstance(matrix, list) or not all(isinstance(mlist, list)
                                               for mlist in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    for mlist in matrix:
        if not all(isinstance(elm, (int, float)) for elm in mlist):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")

    # Testing for row length:
    for mlist in matrix:
        if len(mlist) != rowLen:
            raise TypeError("Each row of the matrix must have the same size")

    # The actual function:
    for mlist in matrix:
        newList = []
        for elm in mlist:
            newList.append(round(elm / div, 2))
        newMatrix.append(newList)

    return newMatrix
