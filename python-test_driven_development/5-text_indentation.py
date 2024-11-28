#!/usr/bin/python3
"""
This module provides a function to print text with indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text to format and print.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define characters that require indentation
    delimiters = {'.', '?', ':'}
    output = ""
    for char in text:
        output += char
        if char in delimiters:
            output += "\n\n"
    # Split and strip each line to remove trailing spaces
    lines = [line.strip() for line in output.split("\n")]
    print("\n".join(lines), end="")
