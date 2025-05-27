#!/usr/bin/python3

"""
A module for training extension of builtin classes.
"""


class VerboseList(list):
    """
    A class for extending the methods of the List class
    """
    def append(self, elm):
        """
        Methods for extending append method by printing the value appended.
        """
        super().append(elm)
        print("Added [{}] to the list.".format((elm)))

    def extend(self, list):
        """
        Methods for extending extend method by printing the size of entension.
        """
        super().extend(list)
        print("Extended the list with [{}] items.".format((len(list))))

    def remove(self, elm):
        """
        Methods for extending extend method by printing the size of entension.
        """
        super().remove(elm)
        print("Removed [{}] from the list.".format(elm))

    def pop(self, idx=-1):
        """
        Methods for extending pop method by printing the index of the
        element removed from the list.
        """
        elm = super().pop(idx)
        print("Popped [{}] from the list.".format(elm))
