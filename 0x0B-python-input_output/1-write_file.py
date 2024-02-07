#!/usr/bin/python3
"""File Writing Module"""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
