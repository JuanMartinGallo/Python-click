import json
import os


def read_json():
    """
    Reads a JSON file and returns its contents.

    Returns:
        list: The contents of the JSON file.
    """
    if not os.path.isfile("data.json"):
        with open("data.json", "w") as f:
            json.dump([], f)
    with open("data.json", "r") as f:
        data = json.load(f)
    return data


def write_json(data):
    """
    Writes the given data to a JSON file.

    Args:
        data (Any): The data to be written to the JSON file.

    Returns:
        None
    """
    with open("data.json", "w") as f:
        json.dump(data, f)
