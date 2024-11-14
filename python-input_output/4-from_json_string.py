#!/usr/bin/python3
"""
This module provides a function to convert a JSON string into a Python
object.

The `from_json_string` function takes a JSON-formatted string as an argument
and returns the corresponding Python data structure.

Functions:
    from_json_string(my_str): Returns the Python object represented by a
    JSON string.
"""

import json


def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert into a Python object.

    Returns:
        object: The Python object obtained from the JSON string.
    """
    return json.loads(my_str)
