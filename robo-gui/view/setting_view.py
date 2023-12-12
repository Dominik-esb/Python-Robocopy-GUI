import customtkinter


class SettingsView(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.btn_save = customtkinter.CTkButton(
            master=self, text="Save", command=lambda: self.save(window=parent))
        self.btn_save.grid(row=1,
                           column=0, columnspan=2, pady=20, padx=20)

        self.appearance_mode_label = customtkinter.CTkLabel(
            master=self, text="Appearance Mode:", anchor="w"
        )
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            master=self,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_optionemenu.grid(
            row=6, column=0, padx=20, pady=(10, 10))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
        self.lift

    def on_closing(self):
        self.parent.destroy()

    def save(self, window):
        window.destroy()
