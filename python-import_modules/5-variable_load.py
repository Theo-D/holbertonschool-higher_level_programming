#!/usr/bin/python3
import variable_load_5

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
