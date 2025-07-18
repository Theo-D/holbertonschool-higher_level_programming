#!/usr/bin/python3

"""
A module for working with mixin classes.
"""


class SwimMixin():
    def swim(self):
        print("The creature swims!")

class FlyMixin():
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
