#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list and saves
them to a JSON file.

It uses the functions `save_to_json_file` and `load_from_json_file` to manage
the JSON file's data, ensuring that each script run adds the arguments to
an existing list in the file or creates a new list if the file does not exist.

Usage:
    ./7-add_item.py <arg1> <arg2> ...

Functions:
    - load_from_json_file(filename): Loads JSON data from a file.
    - save_to_json_file(my_obj, filename): Saves a Python object to a JSON file.
"""

import sys

# Importing the functions from previous tasks
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Try to load the existing list from the file, or start with an empty list
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add command-line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
