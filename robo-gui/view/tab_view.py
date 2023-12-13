"""Tab view module"""
import customtkinter


class MyTabView(customtkinter.CTkTabview):  # pylint: disable=W0223,R0901
    """MyTabView class"""

    def __init__(self, master):
        """initializes the MyTabView class"""
        super().__init__(master)
        self.scrollable_frame = None
        self.scrollable_frame_switches = []
        self.textbox = None
        self.build_tab_view()

    def build_tab_view(self):
        """builds the tab view"""
        self.add_tabs(["Copy", "Analysis"])
        self.configure_tab("Copy", columns=[1, 2, 3], rows=[0, 1, 2])

        self.log_view()
        self.backup_job_list()
        self.create_switches()

    def add_tabs(self, tab_names):
        """adds tabs to the tab view"""
        for name in tab_names:
            self.add(name)

    def configure_tab(self, tab_name, columns=None, rows=None):
        """configures the tab"""
        tab = self.tab(tab_name)
        if columns:
            for col in columns:
                tab.grid_columnconfigure(col, weight=1)
        if rows:
            for row in rows:
                tab.grid_rowconfigure(row, weight=1)

    def log_view(self):
        """creates the log view"""
        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            self.tab("Copy"), label_text="Backup Jobs"
        )
        self.scrollable_frame.grid(
            row=0,
            rowspan=3,
            column=2,
            padx=(20, 0),
            pady=(20, 20),
            sticky="nsew",
        )
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

    def create_switches(self):
        """creates the switches for the log view"""
        for i in range(10):
            switch = customtkinter.CTkSwitch(
                master=self.scrollable_frame, text=f"{i}"
            )
            switch.select()
            switch.grid(row=i, column=0, padx=10, pady=(0, 20), sticky="w")
            self.scrollable_frame_switches.append(switch)

    def backup_job_list(self):
        """creates the backup job list"""
        self.textbox = customtkinter.CTkTextbox(self.tab("Copy"), width=150)
        self.textbox.grid(
            row=1,
            column=1,
            rowspan=2,
            padx=(20, 0),
            pady=(20, 0),
            sticky="nsew",
        )

    def update_log(self, message):
        """updates the log"""
        self.textbox.insert("0.0", f"{message}\n")
