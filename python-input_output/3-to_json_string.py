#!/usr/bin/python3
"""
This module provides a function to convert an object to its JSON string
representation.

The `to_json_string` function takes an object as an argument, converts it
to JSON format, and returns the resulting JSON string.

Functions:
    to_json_string(my_obj): Returns the JSON representation of an object as
    a string.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
        my_obj: The object to convert to JSON format.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
