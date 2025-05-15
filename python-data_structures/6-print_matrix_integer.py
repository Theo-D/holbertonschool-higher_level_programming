#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        idx = 0
        for i in list:
            if idx != len(list) - 1:
                print("{:d}".format(i), end=" ")
                idx += 1
            else:
                print("{:d}".format(i), end ="\n")
