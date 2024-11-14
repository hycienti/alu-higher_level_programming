#!/usr/bin/python3
"""
This module provides a function to create a Python object from a JSON file.

The `load_from_json_file` function takes a filename as an argument, reads
the JSON content from the file, and returns the corresponding Python object.

Functions:
    load_from_json_file(filename): Creates a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the file containing JSON content.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
