"""this module contains the SettingsView class"""
import customtkinter


class BackupCreateView(customtkinter.CTkFrame):
    """SettingsView class"""

    def __init__(self, parent):
        """initializes the backup job create view class"""
        super().__init__(parent)
        self.parent = parent
        # self.tab_view = TabView(master=self)
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ============ configure grid layout (4x4) ============
        self.grid_columnconfigure((3), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=0)
        self.grid_rowconfigure((0, 1, 2, 5), weight=0)
        self.grid_rowconfigure((4), weight=1)

        self.build_settings_view()

    def build_settings_view(self):
        """builds the settings view"""
        source_directory_textbox_label = customtkinter.CTkLabel(
            self,
            text="Source Directory",
            font=customtkinter.CTkFont(size=12, weight="bold"),
        )
        source_directory_textbox_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=(20, 0),
            sticky="w"
        )
        self.source_directory_textbox = customtkinter.CTkTextbox(self, height=28)
        self.source_directory_textbox.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=20,
            pady=(5, 0)
            )

        self.source_directory_btn = customtkinter.CTkButton(self, width=40)
        self.source_directory_btn.grid(row=1, column=2, padx=20, pady=(5, 0))

        destination_directory_textbox_label = customtkinter.CTkLabel(
            self,
            text="Destination Directory",
            font=customtkinter.CTkFont(size=12, weight="bold"),
        )
        destination_directory_textbox_label.grid(
            row=2,
            column=0,
            padx=20,
            pady=(20, 0),
            sticky="w"
        )
        self.destination_directory_textbox = customtkinter.CTkTextbox(self, height=28)
        self.destination_directory_textbox.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=20,
            pady=(5, 0)
            )

        self.destination_directory_btn = customtkinter.CTkButton(self, width=40)
        self.destination_directory_btn.grid(row=3, column=2, padx=20, pady=(5, 0))

        self.btn_save = customtkinter.CTkButton(
            master=self,
            text="Save",
            command=lambda: self.save(window=self.parent),
        )
        self.btn_save.grid(row=5, column=3, pady=20, padx=20, sticky="e")

    def on_closing(self):
        """closes the window"""
        self.parent.destroy()

    def save(self, window):
        """saves the settings"""
        window.destroy()
