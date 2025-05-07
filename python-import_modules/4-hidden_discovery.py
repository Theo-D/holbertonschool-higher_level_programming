#!/usr/bin/python3
import hidden_4

methods = dir(hidden_4)
for names in methods:
    if names[0] != '_':
        print("{}".format(names))
