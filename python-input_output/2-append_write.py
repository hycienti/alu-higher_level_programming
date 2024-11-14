#!/usr/bin/python3
"""
This module provides a function to append a string to the end of a UTF-8
encoded text file.

The `append_write` function takes a filename and a string as arguments, appends
the string to the specified file, and returns the number of characters added.
The function uses Python's `with` statement to ensure safe file handling.

Functions:
    append_write(filename="", text=""): Appends a string to a UTF-8 encoded
    text file and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a UTF-8 encoded text file and returns the number of
    characters added.

    Args:
        filename (str): The name of the file to append to. Defaults to an
        empty string.
        text (str): The string to append to the file. Defaults to an empty
        string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
