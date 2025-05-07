#!/usr/bin/python3
from sys import argv


def main():
    argc = len(argv) - 1
    res = 0
    for i in range(argc):
        res += int(argv[i + 1])
    if argc == 0:
        print("0")
    else:
        print("{:d}".format(res))


if __name__ == "__main__":
    main()
