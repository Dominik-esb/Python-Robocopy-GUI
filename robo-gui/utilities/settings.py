"""Module for reading and writing settings to a file."""
import pickle
from pathlib import Path

SETTINGS_PATH = Path(__file__).parent.parent.joinpath("settings.pickle")


def set(key, value):
    """
    Writes a value to the settings file based on a key. The value can be any type.
    """
    # Open the file and load the data
    try:
        with open(SETTINGS_PATH, "rb") as f:
            data = pickle.load(f)
    except FileNotFoundError:
        data = {}
    # Update the value in the given key
    data[key] = value
    # Save the data back to the file
    with open(SETTINGS_PATH, "wb") as f:
        pickle.dump(data, f)


def get(key):
    """
    Retrieves a value from the settings file based on a key.
    """
    # Open the file and load the data
    try:
        with open(SETTINGS_PATH, "rb") as f:
            data: dict = pickle.load(f)
    except FileNotFoundError:
        return None
    # Return the value at the given key
    return data.get(key)


def delete(key):
    """
    Deletes a value from the settings file based on a key.
    """
    # Open the file and load the data
    try:
        with open(SETTINGS_PATH, "rb") as f:
            data = pickle.load(f)
    except FileNotFoundError:
        return
    # Delete the given key
    del data[key]
    # Save the data back to the file
    with open(SETTINGS_PATH, "wb") as f:
        pickle.dump(data, f)
