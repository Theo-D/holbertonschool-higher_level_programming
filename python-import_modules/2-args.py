#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1

if argc == 0:
    print("0 arguments.")
elif argc < 2:
    print("{} argument:".format(argc))
else:
    print("{} arguments:".format(argc))

for i in range(argc):
    print("{:d}: {}".format(i + 1, argv[i + 1]))
