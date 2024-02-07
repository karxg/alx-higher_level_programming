#!/usr/bin/python3
"""Text File Insertion Module"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each occurrence of a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert after each occurrence
            of the search string.
    """
    text = ""
    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as file:
        file.write(text)
