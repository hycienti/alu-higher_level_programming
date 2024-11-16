#!/usr/bin/python3
"""
This module contains a function that converts a class instance
into a dictionary description suitable for JSON serialization.
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing all serializable attributes of the object.
    """
    return obj.__dict__
