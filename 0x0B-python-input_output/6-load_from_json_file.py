#!/usr/bin/python3
"""JSON File Reading Module"""

import json


def load_from_json_file(filename):
    """Reads a JSON file and returns its content as a Python object.

    Args:
        filename (str): The name of the JSON file to be read.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename) as file:
        return json.load(file)
