#!/usr/bin/python3
"""
This module defines a subclass of the built-in list called MyList.
MyList includes an additional method to print the list in ascending order.
"""


class MyList(list):
    """
    A subclass of list that provides an additional method to print
    the elements of the list in sorted (ascending) order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.
        Assumes all elements are integers.
        """
        print(sorted(self))
