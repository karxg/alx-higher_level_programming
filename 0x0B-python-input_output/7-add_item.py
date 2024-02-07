#!/usr/bin/python3
"""Argument Saving Module"""

from sys import argv

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

FILENAME = "add_item.json"

try:
    # Try to load existing JSON data from file
    json_obj = load_from_json_file(FILENAME)
    # Append command line arguments to loaded JSON object
    json_obj += argv[1:]
    # Save updated JSON object to file
    save_to_json_file(json_obj, FILENAME)

except FileNotFoundError:
    # If file does not exist, create new JSON file with command line arguments
    save_to_json_file(argv[1:], FILENAME)
