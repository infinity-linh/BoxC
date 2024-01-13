import customtkinter
from chapter.main_window.audio.gui_audio import gui_audio
from chapter.main_window.visualize.vizualize_gui import gui_vizualize


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App_main(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("BoxC")
        self.geometry(f"{1100}x{580}")
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.audio_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        # self.audio_frame.grid(row=0, column=1, columnspan=4, rowspan=3, sticky="nsew")

        self.visual_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        # self.audio_frame.grid(row=0, column=1, columnspan=4, rowspan=3, sticky="nsew")

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Audio Labeling", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.protocol("WM_DELETE_WINDOW", self.on_close)


        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Audio", command=self.audio_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text="Image", command=self.image_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Visualize", command=self.visual_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        
    def on_close(self):
        # Thực hiện các thao tác trước khi đóng cửa sổ (nếu cần)
        self.destroy()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    def audio_button_event(self):
        self.visual_frame.grid_forget()
        self.audio_frame.grid(row=0, column=1, columnspan=4, rowspan=3, sticky="nsew")
        self.config_gui_audio = gui_audio(self.audio_frame)
        # self.sidebar_button_1.configure()
        print("sidebar_button click")
    def image_button_event(self):
        self.audio_frame.grid_forget() 
    def visual_button_event(self):
        self.audio_frame.grid_forget()
        self.visual_frame.grid(row=0, column=1, columnspan=4, rowspan=3, sticky="nsew")
        self.config_gui_vizual = gui_vizualize(self.visual_frame)
        pass
