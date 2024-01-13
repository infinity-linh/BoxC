import customtkinter
from tkinter import filedialog as fd
from chapter.main_window.audio.audio_process import choose_file_audio, list_file_in_folder
from customtkinter.windows.CtkListbox import CTkListbox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
import tkinter
import seaborn as sns
from datetime import date
import calendar
import pandas as pd


class gui_vizualize(customtkinter.CTk):
    def __init__(self, gui):
        super().__init__()
        self.data = {}
        self.data_month = []
        self.today = date.today()
        _, self.days = calendar.monthrange(self.today.year, self.today.month)
        self.insert_database()
        sns.set()

        figure = Figure(figsize=(10, 6))

        ax = figure.subplots()
        ax = sns.barplot(self.data, x="days", y="pay", ax=ax, errorbar=None)
        # ax.set_xticklabels(ax.get_xticklabels(), rotation=60, horizontalalignment="center")
        self.ui = gui
        self.ui.grid_columnconfigure(2, weight=1)
        self.ui.grid_rowconfigure(2, weight=1)
        self.frame_grap = customtkinter.CTkFrame(self.ui, corner_radius=10)
        self.frame_grap.grid(row=0, column=0, columnspan = 4, padx=(20, 20), pady=(20, 0), sticky="nsew")
        # canvas = FigureCanvasTkAgg(fig, master=self.frame_grap)
        # canvas.draw()
        # canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.entry = customtkinter.CTkEntry(self.ui, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        canvas = FigureCanvasTkAgg(figure, master=self.frame_grap)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        # call key press event


        # self.config_grid(self.frame_audio)

        # # self.ui.grid_columnconfigure((1, 4, 2), weight=1)
        # self.frame_list = customtkinter.CTkFrame(self.ui, width=100, corner_radius=10)
        # self.frame_list.grid(row=0, column=4, rowspan=4, padx=(0, 20), pady=(20, 0), sticky="nsew")
        # self.config_grid(self.frame_list)
        # self.listbox = CTkListbox(self.frame_list, command=self.show_value)
        # self.listbox.pack(fill="both", expand=True, padx=10, pady=10)
        # self.listbox.rowconfigure(0, weight=1)

        # #phần văn bản của app
        # self.frame_text = customtkinter.CTkFrame(self.ui, corner_radius=5)
        # self.frame_text.grid(row=1, column=0, columnspan = 4, padx=(20, 20), pady=(20, 20), sticky="nsew")
        # self.config_grid(self.frame_text)
        # self.textbox = customtkinter.CTkTextbox(self.frame_text)
        # self.textbox.grid(row=1, column=0, columnspan = 5, rowspan = 3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        # self.textbox.insert('0.0', 'toilalinh03superbot')

        # self.name_audio_frame = customtkinter.CTkFrame(self.frame_audio)
        # self.name_audio_frame.grid(row=0, column=1, columnspan = 4,rowspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        # self.name_audio_frame.grid_columnconfigure(2, weight=1)
        # self.name_audio_frame.grid_rowconfigure(2, weight=1)
        # self.label_audio = customtkinter.CTkLabel(master=self.name_audio_frame, text="Name audio")
        # self.label_audio.grid(row=0, column=0, padx=(10, 10), pady=(10, 5), sticky="")
        # self.slider_2 = customtkinter.CTkSlider(self.name_audio_frame,from_=0, height=100, to=100, number_of_steps=100, orientation="vertical", command=self.set_vol)
        # self.slider_2.grid(row=0, column=4, rowspan=1, padx=(10, 10), pady=(0, 0), sticky="ns")
        # # self.config_grid(self.name_audio_frame)


        # self.slider_progressbar_frame = customtkinter.CTkFrame(self.name_audio_frame, fg_color="transparent")
        # self.slider_progressbar_frame.grid(row=1, column=0, columnspan = 4, padx=(0, 0), pady=(0, 0), sticky="nsew")
        # self.slider_progressbar_frame.grid_columnconfigure(4, weight=1)
        # self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        # self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        # self.progressbar_2.grid(row=1, column=0, padx=(10, 10), pady=(0, 0), sticky="ew")

        # self.input_button_back = customtkinter.CTkButton(self.slider_progressbar_frame,width=50, text="<", command=self.opendir)
        # self.input_button_back.grid(row=0, column=0, padx=(10, 10), pady=(0, 0))
        # self.input_button_next = customtkinter.CTkButton(self.slider_progressbar_frame,width=50, text=">", command=self.create_list)
        # self.input_button_next.grid(row=0, column=2, padx=(10, 10), pady=(0, 0))
        # self.input_button_play = customtkinter.CTkButton(self.slider_progressbar_frame,width=50, text="Play", command=self.play_audio)
        # self.input_button_play.grid(row=0, column=1, padx=(10, 10), pady=(0, 0))
        # self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=100, number_of_steps=100, command=self.set_pos)
        # self.slider_1.grid(row=0, column=3, columnspan = 4, padx=(10, 10), pady=(0, 0), sticky="ew")
        # self.slider_progressbar_frame.bind("<KeyPress>", self.on_key_press)




        # self.button_frame_1 = customtkinter.CTkFrame(self.frame_audio)
        # self.button_frame_1.grid(row=1, column=1, columnspan = 4, padx=(10, 10), pady=(10, 10), sticky="nsew")
        # self.button_frame_1.grid_columnconfigure(2, weight=1)
        # self.button_frame_1.grid_rowconfigure(2, weight=1)

        # self.combobox_3 = customtkinter.CTkComboBox(self.button_frame_1, width=300, values=['...'])
        # self.combobox_3.grid(row=0, column=0, rowspan = 1, padx=(10, 10), pady=(10, 10))
        # self.input_button_3 = customtkinter.CTkButton(self.button_frame_1, text="Choose", command=self.opendir)
        # self.input_button_3.grid(row=0, column=1,  padx=(10, 10), pady=(10,10))
        # self.combobox_4 = customtkinter.CTkComboBox(self.button_frame_1, width=300, values=['...'])
        # self.combobox_4.grid(row=1, column=0,  padx=(10, 10), pady=(10, 10))
        # self.input_button_4 = customtkinter.CTkButton(self.button_frame_1, text="Save", command=self.opensave)
        # self.input_button_4.grid(row=1, column=1, padx=(10, 10), pady=(10,10))

    def insert_database(self):
        self.data = {}
        days = []
        months = []
        years = []
        pay_in_day = []
        for i in range(self.days):
            day = '0'*(2-len(str(i+1)))+str(i+1) 
            month = '0'*(2-len(str(self.today.month)))+str(self.today.month) 
            year = f"{self.today.year}"
            days.append(day)
            months.append(month)
            years.append(year)

        # print("Ngay hien tai:", today)
        self.data["days"] = days
        self.data["months"] = months
        self.data["years"] = years

        for i in range(self.days):
            pay_in_day.append(i)
        self.data["pay"] = pay_in_day
        self.data["earn"] = pay_in_day
        self.data_month = pd.DataFrame(data=self.data)


