#!/usr/bin/python3
"""String to JSON Module"""

import json


def to_json_string(my_obj):
    """Converts a Python object to its JSON representation.

    Args:
        my_obj: The Python object to be converted.

    Returns:
        str: The JSON representation of the input Python object.
    """
    return json.dumps(my_obj)
