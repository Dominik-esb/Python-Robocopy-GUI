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

    def on_closing(self):
        self.parent.destroy()

    def save(self, window):
        window.destroy()
