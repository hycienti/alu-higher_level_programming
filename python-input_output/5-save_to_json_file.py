#!/usr/bin/python3
"""
This module provides a function to save a Python object to a text file in
JSON format.

The `save_to_json_file` function takes a Python object and a filename as
arguments, converts the object to JSON format, and writes it to the specified
file.

Functions:
    save_to_json_file(my_obj, filename): Writes a Python object to a text file
    as a JSON string.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using JSON representation.

    Args:
        my_obj: The Python object to serialize and write to the file.
        filename (str): The name of the file to write the JSON representation
        to.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
