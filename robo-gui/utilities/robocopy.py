"""Module builds a robocopy command"""
import pathlib

from utilities.json_handler import JasonHandler


class RobocopyCommandBuilder:
    """RobocopyCommandBuilder class"""
    def __init__(self, backup_job_name):
        """initializes the RobocopyCommandBuilder class"""
        self.dictionary = JasonHandler.load_json(
                pathlib.Path(__file__)
                .parent.parent.resolve()
                .joinpath("config", "backup_options.json")
            )["checkbox_values"]

        self.backup_job_name = backup_job_name

    def search(self, keyword):
        """searches the dictionary for a keyword"""
        if keyword in self.dictionary:
            return self.dictionary[keyword]
        else:
            return None
