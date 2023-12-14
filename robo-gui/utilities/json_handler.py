"""This module contains functions for loading and saving json files"""
import json


class JasonHandler:
    """Class to handle Processes"""

    def __init__(self):
        pass

    def load_json(file_path):
        """loads a json file by file path (file_path)"""
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def save_json(file_path, data):
        """saves a json file by file path (file_path) and data (data)"""
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
