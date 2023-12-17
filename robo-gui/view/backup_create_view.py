"""this module contains the SettingsView class"""
import tkinter.filedialog

import customtkinter
import utilities.robocopy as robocopy
import utilities.settings as settings
from CTkToolTip import CTkToolTip


class BackupCreateView(customtkinter.CTkFrame):
    """SettingsView class"""

    def __init__(self, parent):
        """initializes the backup job create view class"""
        super().__init__(parent)
        self.parent = parent
        self.textboxes = {}
        self.robocopy_arguments = robocopy.get_robocopy_arguments()
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ============ configure grid layout (4x4) ============
        self.grid_columnconfigure((3), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=0)
        self.grid_rowconfigure((0, 1, 2, 7), weight=0)
        self.grid_rowconfigure((6), weight=1)

        self.build_settings_view()
        self.create_robocopy_arguments_frame()
        self.create_arguments_list()

    def build_settings_view(self):
        """builds the settings view"""
        self.create_label(
            text="Backup Job Name", row=0, column=0, padx=20, pady=(20, 0)
        )
        self.create_textbox(
            textbox_name="backup_job_name",
            height=28,
            row=1,
            column=0,
            columnspan=2,
            padx=20,
            pady=(5, 0),
        )
        self.create_label(
            text="Source Directory", row=2, column=0, padx=20, pady=(20, 0)
        )
        self.create_textbox(
            textbox_name="source_directory",
            height=28,
            row=3,
            column=0,
            columnspan=2,
            padx=20,
        )

        self.source_directory_btn = customtkinter.CTkButton(
            self,
            width=20,
            text="+",
            command=self.__on_source_directory_btn_clicked,
        )
        self.source_directory_btn.grid(row=3, column=2, padx=20, pady=(5, 0))

        self.create_label(
            text="Destination Directory",
            row=4,
            column=0,
            padx=20,
            pady=(20, 0),
        )

        self.create_textbox(
            textbox_name="destination_directory",
            row=5,
            column=0,
            columnspan=2,
            padx=20,
            pady=(5, 0),
        )

        self.destination_directory_btn = customtkinter.CTkButton(
            self,
            width=20,
            text="+",
            command=self.__on_destination_directory_btn_clicked,
        )
        self.destination_directory_btn.grid(
            row=5, column=2, padx=20, pady=(5, 0)
        )

        self.btn_save = customtkinter.CTkButton(
            master=self,
            text="Save",
            command=lambda: self.save(window=self.parent),
        )
        self.btn_save.grid(row=7, column=3, pady=20, padx=20, sticky="e")

    def create_label(
        self,
        text,
        row=0,
        rowspan=1,
        column=0,
        columnspan=1,
        padx=20,
        pady=(20, 0),
    ):
        """creates a label"""
        label = customtkinter.CTkLabel(
            self,
            text=text,
            font=customtkinter.CTkFont(size=12, weight="bold"),
        )
        label.grid(
            row=row,
            rowspan=rowspan,
            column=column,
            columnspan=columnspan,
            padx=padx,
            pady=pady,
            sticky="w",
        )

    def create_textbox(
        self,
        textbox_name,
        height=28,
        row=0,
        rowspan=1,
        column=0,
        columnspan=1,
        padx=20,
        pady=(5, 0),
    ):
        """creates a textbox"""
        textbox = customtkinter.CTkTextbox(self, height=height)
        textbox.grid(
            row=row,
            rowspan=rowspan,
            column=column,
            columnspan=columnspan,
            padx=padx,
            pady=pady,
        )
        self.textboxes[textbox_name] = textbox

    def create_robocopy_arguments_frame(self):
        """creates the robocopy arguments frame"""
        self.robocopy_arguments_frame = customtkinter.CTkScrollableFrame(
            self, label_text="Robocopy Arguments"
        )
        self.robocopy_arguments_frame.grid(
            row=0, rowspan=7, column=3, padx=20, pady=(20, 0), sticky="nsew"
        )

    def create_arguments_list(self):
        """creates the arguments list"""
        search = customtkinter.CTkEntry(
            self.robocopy_arguments_frame, placeholder_text="Search"
        )
        search.grid(row=0, column=0, padx=(20, 20), pady=(20, 0), sticky="we")
        search.bind(
            "<KeyRelease>",
        )  # lambda e: self.search_package(self.entry.get()) TODO: fix search
        for i, (key, value) in enumerate(self.robocopy_arguments.items()):
            radio_button = customtkinter.CTkRadioButton(
                self.robocopy_arguments_frame, text=f"{key} - {value}"
            )
            radio_button.grid(
                row=i + 1, column=0, padx=20, pady=(20, 0), sticky="w"
            )
            # tooltip = CTkToolTip(radio_button, message=f"{value}")
            # TODO: fix tooltip

    def __on_source_directory_btn_clicked(self):
        """opens a filedialog to select a source directory"""
        path = tkinter.filedialog.askdirectory()
        source_directory_textbox = self.textboxes["source_directory"]
        source_directory_textbox.delete("1.0", "end")
        source_directory_textbox.insert("end", path)

    def __on_destination_directory_btn_clicked(self):
        """opens a filedialog to select a destination directory"""
        path = tkinter.filedialog.askdirectory()
        source_directory_textbox = self.textboxes["destination_directory"]
        source_directory_textbox.delete("1.0", "end")
        source_directory_textbox.insert("end", path)

    def on_closing(self):
        """closes the window"""
        self.parent.destroy()

    def save(self, window):
        """saves the settings"""
        backup_job_name = self.textboxes["backup_job_name"].get(
            "1.0", "end-1c"
        )

        if not settings.get(backup_job_name):
            settings.set(
                backup_job_name,
                [
                    self.textboxes["source_directory"].get("1.0", "end-1c"),
                    self.textboxes["destination_directory"].get(
                        "1.0", "end-1c"
                    ),
                ],
            )
        window.destroy()
