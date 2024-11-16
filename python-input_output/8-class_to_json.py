#!/usr/bin/python3
"""
This module provides a function to convert a class instance
into a dictionary for JSON serialization.
"""

def class_to_json(obj):
    """
    Converts a class instance to a dictionary for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary of the object's serializable attributes.
    """
    return obj.__dict__
