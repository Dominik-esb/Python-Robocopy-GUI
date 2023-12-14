"""Tab view module"""
import pathlib

import customtkinter
from utilities.json_handler import JasonHandler  # pylint: disable=import-error

# from utilities.log_helper import Logger  # pylint: disable=import-error


class TabView(customtkinter.CTkTabview):  # pylint: disable=W0223,R0901
    """MyTabView class"""

    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        """creates a new instance of the Logger class"""
        if cls._instance is None:
            cls._instance = super(TabView, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, master):
        """initializes the MyTabView class"""
        super().__init__(master)

        if self._initialized:
            return
        self._initialized = True

        self.scrollable_frame = None
        self.scrollable_frame_switches = []
        self.textbox = None
        try:
            self.backup_job_list = JasonHandler.load_json(
                pathlib.Path(__file__)
                .parent.parent.resolve()
                .joinpath("config", "backup_options.json")
            )["checkbox_values"]
        except FileNotFoundError:
            print("File not found")
            self.backup_job_list = []

        self.build_tab_view()

    def build_tab_view(self):
        """builds the tab view"""
        # self.logger.add_to_log("Building tab view...")

        self.add_tabs(["Copy", "Analysis"])
        self.configure_tab(
            "Copy", columns=[[1, 2], [0, 0]], rows=[[0, 1], [1, 1]]
        )
        self.configure_tab(
            "Analysis", columns=[[1, 2], [0, 0]], rows=[[0, 1], [1, 1]]
        )

        self.log_view()
        self.create_backup_job_list()
        self.create_switches()

    def add_tabs(self, tab_names):
        """adds tabs to the tab view"""
        for name in tab_names:
            self.add(name)

    def configure_tab(
        self,
        tab_name,
        columns=None,
        rows=None,
    ):
        """configures the tab"""
        tab = self.tab(tab_name)
        if columns:
            for col, weight in columns:
                tab.grid_columnconfigure(col, weight=weight)
        if rows:
            for row, weight in rows:
                tab.grid_rowconfigure(row, weight=weight)

    def create_backup_job_list(self):
        """creates the log view"""
        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            self.tab("Copy"), label_text="Backup Jobs"
        )
        self.scrollable_frame.grid(
            row=0,
            rowspan=3,
            column=2,
            padx=(0, 20),
            pady=(20, 20),
            sticky="nsew",
        )
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

    def create_switches(self):
        """creates the switches for the log view"""
        for i, value in enumerate(self.backup_job_list):
            switch = customtkinter.CTkSwitch(
                master=self.scrollable_frame, text=value, width=150
            )
            switch.select()
            switch.grid(row=i, column=0, padx=10, pady=(0, 20), sticky="w")
            self.scrollable_frame_switches.append(switch)

    def log_view(self):
        """creates the backup job list"""
        self.textbox = customtkinter.CTkTextbox(self.tab("Copy"), width=150)
        self.textbox.grid(
            row=1,
            column=1,
            rowspan=2,
            padx=(20, 0),
            pady=(20, 20),
            sticky="nsew",
        )

    def update_log(self, message):
        """updates the log"""
        self.textbox.insert("end", f"{message}\n")
