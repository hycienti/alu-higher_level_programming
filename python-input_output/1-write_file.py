#!/usr/bin/python3
"""
This module provides a function to write a string to a UTF-8 encoded text file.

The `write_file` function takes a filename and a string as arguments, writes the
string to the specified file, and returns the number of characters written. The
function uses Python's `with` statement to ensure safe file handling.

Functions:
    write_file(filename="", text=""): Writes a string to a UTF-8 encoded text
    file and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 encoded text file and returns the number of
    characters written.

    Args:
        filename (str): The name of the file to write to. Defaults to an empty
        string.
        text (str): The string to write to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
