#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves them to a file in JSON format.

The list is stored in a file named `add_item.json`.
It uses two functions:
- save_to_json_file: Saves a Python object to a JSON file.
- load_from_json_file: Loads a Python object from a JSON file.

If the file does not exist, it is created.
"""

import sys
from os import path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

if path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
