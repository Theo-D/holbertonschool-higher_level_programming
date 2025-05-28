#!/usr/bin/python3

"""
A module for building an iterator.
"""


class CountedIterator():
    """
    A class that extends the built-in iterator obtained from the
    iter function.
    """
    def __init__(self, iterator):
        self.__iterator = iter(iterator)
        self.__count = 0

    def __next__(self):
        try:
            elm = next(self.__iterator)
        except:
            raise StopIteration
        else:
            self.__count += 1
            return elm

    def get_count(self):
        return self.__count
