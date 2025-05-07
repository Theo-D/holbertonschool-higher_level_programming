#!/usr/bin/python3
import itertools
for i, j in itertools.product(range(0, 10), range(0, 10)):
    if i < 9 or j < 9:
        print("{:d}{:d},".format(i, j), end=" ")
    else:
        print("{:d}{:d}".format(i, j))
