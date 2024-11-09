#!/usr/bin/python3
"""
This module provides a utility function to list all available attributes
and methods of a given object for introspection purposes.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of attribute and method names.
    """
    return dir(obj)
