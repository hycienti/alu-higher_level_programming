#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list and saves
them to a JSON file named `add_item.json`.

The script uses two functions:
    - `save_to_json_file`: Saves a Python object to a file in JSON format.
    - `load_from_json_file`: Loads a Python object from a JSON file.

If the `add_item.json` file already exists, the script loads its contents as
a list, appends the command-line arguments to it, and saves the updated list
back to the file. If the file does not exist, it creates the file with the
new list of arguments.

Usage:
    ./7-add_item.py <arg1> <arg2> ...

Functions:
    - load_from_json_file(filename): Loads JSON data from a file.
    - save_to_json_file(my_obj, filename): Saves a Python object to a JSON file.
"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    # Try to load the existing list from the file
    items = load_from_json_file(filename)
except FileNotFoundError:
    # Initialize an empty list if the file doesn't exist
    items = []

# Append command-line arguments (excluding the script name) to the list
items.extend(sys.argv[1:])

# Save the updated list back to the JSON file
save_to_json_file(items, filename)

