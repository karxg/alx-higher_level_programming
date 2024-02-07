#!/usr/bin/python3
"""JSON File Writing Module"""

import json


def save_to_json_file(my_obj, filename):
    """Write a Python object to a JSON file.

    Args:
        my_obj: The Python object to be written to the file.
        filename (str): The name of the file to write.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
