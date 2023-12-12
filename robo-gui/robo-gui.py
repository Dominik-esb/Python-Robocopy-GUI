import tkinter

import customtkinter
from view import *

customtkinter.set_appearance_mode(
    "System"
)  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    WIDTH = 1100
    HEIGHT = 580
    DEFAULT_GRAY = ("gray50", "gray30")

    def __init__(self, test: bool = False):
        super().__init__()
        # self.__init_settings()

        if not test:

            self.build_ui()

    def build_ui(self):
        # ============ configure window ============
        self.title("Robocopy GUI")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.update()
        self.minsize(self.winfo_width(), self.winfo_height())

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ============ configure grid layout (4x4) ============
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # ============ create sidebar frame with widgets ============
        self.sidebar_frame = customtkinter.CTkFrame(
            self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame,
            text="Robo-GUI",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_start = customtkinter.CTkButton(
            self.sidebar_frame, command=self.sidebar_button_event,
            fg_color="#017550", hover_color="#014f42",
        )
        self.sidebar_button_start.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_stop = customtkinter.CTkButton(
            self.sidebar_frame, command=self.sidebar_button_event,
            fg_color="#7e0030", hover_color="#60002d",
        )
        self.sidebar_button_stop.grid(row=2, column=0, padx=20, pady=10)

        # ============ Settings Button ============
        self.sidebar_button_settings = customtkinter.CTkButton(
            master=self.sidebar_frame,
            # fg_color="#2a2d2e",
            # hover_color=self.DEFAULT_GRAY,
            text="Settings",
            # image=self.img_settings,
            command=self.__on_settings_clicked,
        )
        self.sidebar_button_settings.grid(
            row=8, column=0, padx=20, pady=(10, 20))

        self.scaling_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Settings menue:", anchor="w"
        )
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))

        # self.scaling_optionemenu = customtkinter.CTkOptionMenu(
        #     self.sidebar_frame,
        #     values=["80%", "90%", "100%", "110%", "120%"],
        #     command=self.change_scaling_event,
        # )
        # self.scaling_optionemenu.grid(row=8, column=0, padx=20,
        # pady=(10, 20))

        # ============ create textbox ============
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, rowspan=2, padx=(
            20, 0), pady=(20, 0), sticky="nsew")

        # ============ create tabview ============
        self.scrollable_frame_test = customtkinter.CTkFrame(
            self, width=140, corner_radius=0)
        self.scrollable_frame_test.grid(
            row=2, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew"
        )
        self.scrollable_frame_test.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_test_switches = []
        for i in range(3):
            switch = customtkinter.CTkSwitch(
                master=self.scrollable_frame_test, text=f"CTkSwitch {i}"
            )
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_test_switches.append(switch)

        # ============ create scrollable frame ============
        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            self, label_text="Backup Jobs"
        )
        self.scrollable_frame.grid(
            row=0, rowspan=3, column=2, padx=(20, 0), pady=(20, 20), sticky="nsew"
        )
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        for i in range(100):
            switch = customtkinter.CTkSwitch(
                master=self.scrollable_frame, text=f"CTkSwitch {i}"
            )
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)

        # ============ set default values ============
        self.sidebar_button_start.configure(text="Start Copy")
        self.sidebar_button_stop.configure(text="Stop Copy")
        self.scrollable_frame_switches[0].select()
        self.scrollable_frame_switches[4].select()
        # self.scaling_optionemenu.set("100%")
        self.textbox.insert(
            "0.0",
            "Log\n\n"
        )

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    # ============ Button Handlers ============
    def __on_settings_clicked(self):
        window = customtkinter.CTkToplevel(master=self)
        window.geometry("540x287")
        window.title("Settings")
        view = SettingsView(parent=window)
        view.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        # Workaround for bug where main window takes focus
        window.after(100, window.lift)

    # ============ Misc Handlers ============

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
