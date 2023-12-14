"""module handling the logging"""
import datetime
import os
import pathlib

# pylint: disable=import-error


class Logger:
    """Logger class"""

    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        """creates a new instance of the Logger class"""
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(
        self,
        tab_view,
        log_directory=pathlib.Path(__file__)
        .parent.resolve()
        .joinpath("utilities", "logs"),
    ):
        """initializes the Logger class"""

        if self._initialized:
            return
        self._initialized = True

        self.log_directory = log_directory
        self.logfile = self._generate_logfile_name()
        self.tab_view = tab_view
        self.timestamp = None
        self.log_entry = None

    def _generate_logfile_name(self):
        """generates the logfile name"""
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        return os.path.join(self.log_directory, f"logfile_{timestamp}.txt")

    def create_initial_logfile(self):
        """creates the initial logfile"""
        with open(self.logfile, "w", encoding="utf-8") as file:
            file.write("Initial Logfile\n")

    def add_to_log(self, message):
        """adds a message to the logfile"""

        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log_entry = f"{self.timestamp} - {message}\n"
        self.tab_view.update_log(self.log_entry)
        try:
            with open(self.logfile, "a", encoding="utf-8") as file:
                file.write(self.log_entry)
        except FileNotFoundError:
            self.create_initial_logfile()

    def get_log(self):
        """returns the logfile as a string"""
        try:
            with open(self.logfile, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError as e:
            return f"Log file not found: {e}"
