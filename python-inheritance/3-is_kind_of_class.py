#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of
a specified class or an instance of a class that inherited from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of the specified class, or
    if the object is an instance of a class that inherited from the specified
    class; otherwise, returns False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance or inherits from a_class, False otherwise.
    """
    return isinstance(obj, a_class)
