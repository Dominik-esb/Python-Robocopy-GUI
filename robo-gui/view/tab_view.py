"""Tab view module"""
import pathlib

import customtkinter
from utilities.json_handler import JasonHandler  # pylint: disable=import-error
from utilities.smart_handler import Smart  # pylint: disable=import-error
from view.backup_create_view import BackupCreateView

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

        self.smart = Smart()

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
            "Analysis", columns=[[0, 1], [0, 0]], rows=[[0, 1], [1, 1]]
        )

        self.log_view()
        self.create_backup_job_frame()
        self.create_add_backup_job_button()
        self.create_backup_job_list_switches()
        self.create_smart_combobopx()

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

    # ============ Copy Tab ============

    def create_backup_job_frame(self):
        """creates the backup job list"""
        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            self.tab("Copy"), label_text="Backup Jobs"
        )
        self.scrollable_frame.grid(
            row=0,
            rowspan=3,
            column=2,
            padx=(0, 20),
            pady=(20, 5),
            sticky="nsew",
        )
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

    def create_add_backup_job_button(self):
        """creates add Button"""
        add_backup_job_button = customtkinter.CTkButton(
            master=self.tab("Copy"),
            text="Add Backup Job",
            command=self.__on_create_back_clicked,
        )
        add_backup_job_button.grid(
            row=3, column=2, padx=10, pady=(0, 20), sticky="nsew"
        )

    def create_backup_job_list_switches(self):
        """creates switches for backup jobs"""
        for i, value in enumerate(self.backup_job_list):
            switch = customtkinter.CTkSwitch(
                master=self.scrollable_frame, text=value, width=150
            )
            switch.select()
            switch.grid(row=i + 1, column=0, padx=10, pady=(0, 20), sticky="w")
            self.scrollable_frame_switches.append(switch)

    def add_backup_job_list_switches(self, name):
        """adds switches for backup jobs"""
        switch = customtkinter.CTkSwitch(
            master=self.scrollable_frame, text=name, width=150
        )
        switch.select()
        switch.grid(row=1, column=0, padx=10, pady=(0, 20), sticky="w")
        self.scrollable_frame_switches.append(switch)

    def log_view(self):
        """creates the log view"""
        self.textbox = customtkinter.CTkTextbox(self.tab("Copy"), width=150)
        self.textbox.grid(
            row=1,
            column=1,
            rowspan=3,
            padx=(20, 0),
            pady=(20, 20),
            sticky="nsew",
        )

    def update_log(self, message):
        """updates the log"""
        self.textbox.insert("end", f"{message}\n")

    # ============ Analysis Tab ============

    def create_smart_combobopx(self):
        """creates the smart combobox"""
        smart_combobox = customtkinter.CTkComboBox(
            master=self.tab("Analysis"),
            values=["option 1", "option 2"],
        )
        smart_combobox.grid(
            row=1, column=1, padx=10, pady=(20, 20), sticky="w"
        )

    # ============ Button Handlers ============

    def __on_create_back_clicked(self):
        """Handle click"""
        window = customtkinter.CTkToplevel(master=self)
        window.geometry("954x487")
        window.title("Add Backup")
        view = BackupCreateView(parent=window)
        view.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        # Workaround for bug where main window takes focus
        window.after(100, window.lift)
