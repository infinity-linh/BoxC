from tkinter import filedialog as fd
import customtkinter


class gui_text(customtkinter.CTk):
    def __init__(self, gui):
        super().__init__()
        self.ui = gui

        self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
