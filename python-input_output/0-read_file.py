#!/usr/bin/python3
"""
This module provides a function to read and print the content of a UTF-8
encoded text file.

The `read_file` function takes a filename as an argument, opens the file in
read mode with UTF-8 encoding, and prints its contents to stdout. This
function uses Python's `with` statement to ensure safe file handling.

Functions:
    read_file(filename=""): Reads a UTF-8 encoded text file and prints its
    content to stdout.
"""

def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its content to stdout.
    
    Args:
        filename (str): The name of the file to read. Defaults to an empty
        string.
        
    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
