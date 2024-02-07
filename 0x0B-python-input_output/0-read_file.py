#!/usr/bin/python3
"""File Reading Module"""


def read_file(filename=""):
    """Reads the contents of a file and prints them.

    Args:
        filename (str): The path to the file to be read.
    """
    with open(filename, encoding="utf-8") as file:
        read_data = file.read()
        print(read_data, end="")
