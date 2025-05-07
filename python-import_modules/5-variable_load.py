#!/usr/bin/python3
from variable_load_5 import a
# import variable_load_5


def main():
    print("{}".format(a))


"""
    variables = []

    for name in dir(variable_load_5):
        if name.startswith('__'):
            continue
        var = getattr(variable_load_5, name)
        if not callable(var):
            variables.append(name)

    for varName in variables:
        val = getattr(variable_load_5, varName)
        print("{}".format(val))
 """
if __name__ == "__main__":
    main()
