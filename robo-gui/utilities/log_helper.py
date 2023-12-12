# logger_module.py

import datetime
import os
import pathlib


class Logger:
    def __init__(self, log_directory=pathlib.Path(__file__).parent.resolve()
                 .joinpath(
            "utilities", "logs")):
        self.log_directory = log_directory
        self.logfile = self._generate_logfile_name()

    def _generate_logfile_name(self):
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        return os.path.join(self.log_directory, f"logfile_{timestamp}.txt")

    def create_initial_logfile(self):
        with open(self.logfile, 'w') as file:
            file.write("Initial Logfile\n")

    def add_to_log(self, message):
        with open(self.logfile, 'a') as file:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"{timestamp}: {message}\n")

    def get_log(self):
        try:
            with open(self.logfile, 'r') as file:
                return file.read()
        except FileNotFoundError as e:
            return "Log file not found."
