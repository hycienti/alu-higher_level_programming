#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of
a class that inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise, returns False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
        False if it is an instance of a_class itself or not related at all.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
