#!/usr/bin/python3
"""
This script takes all command-line arguments, adds them to a Python list,
and saves the list to a file in JSON format. The file used is `add_item.json`.

If the file does not exist, it is created. The list is updated persistently
with each execution of the script.

The script relies on two helper functions:
- save_to_json_file: Saves a Python object to a file in JSON format.
- load_from_json_file: Loads a Python object from a file in JSON format.

Author: Your Name
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
