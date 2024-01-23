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
from tkinter import ttk


class vizual_graph(customtkinter.CTk):
    def __init__(self, gui):
        super().__init__()
        self.data_frame = None
        self.data_plan = {}
        self.data_base = {}
        self.frame_insert = gui
        
        self._optionemenu = customtkinter.CTkOptionMenu(self.frame_insert, values=["Bar", "Pie", "Line", "Table"], command=self.control_graph)
        self._optionemenu.grid(row=0, column=0, padx=(20, 20), pady=(20, 0))
        self.day_current = customtkinter.CTkEntry(self.frame_insert, placeholder_text="CTkEntry")
        self.day_current.grid(row=0, column=1, columnspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.total_money_label = customtkinter.CTkLabel(self.frame_insert, text="Total money:", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.total_money_label.grid(row=1, column=0, columnspan = 1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.total_money = customtkinter.CTkEntry(self.frame_insert, placeholder_text="0"*10, font=customtkinter.CTkFont(size=20, weight="bold"), state="normal")
        self.total_money.grid(row=1, column=1, columnspan = 1, padx=(20, 20), pady=(20, 0), sticky="nsew")


        self.pay_money_label = customtkinter.CTkLabel(self.frame_insert, text="Pay money:", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.pay_money_label.grid(row=2, column=0, columnspan = 1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.pay_money = customtkinter.CTkEntry(self.frame_insert, placeholder_text="Nhập số tiền mất hôm nay", font=customtkinter.CTkFont(size=10, weight="normal"))
        self.pay_money.grid(row=2, column=1, columnspan = 1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.pay_money.bind("<Return>", self.updata_database)

        self.earn_money_label = customtkinter.CTkLabel(self.frame_insert, text="Earn money:", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.earn_money_label.grid(row=3, column=0, columnspan = 1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.earn_money = customtkinter.CTkEntry(self.frame_insert, placeholder_text="Nhập số tiền kiếm được hôm nay", font=customtkinter.CTkFont(size=10, weight="normal"))
        self.earn_money.grid(row=3, column=1, columnspan = 1, padx=(20, 20), pady=(20, 0), sticky="nsew")
    
    
    def updata_database(self, event):
        self.day_current.get()
        self.today = date.today()
        _, self.days = calendar.monthrange(self.today.year, self.today.month)

        try:
            year_base = self.data_base[str(self.today.year)]
        except:
            self.data_base[str(self.today.year)] = {}
            year_base = self.data_base[str(self.today.year)]

        try:
            month_base = year_base[str(self.today.month)]
        except:
            year_base[str(self.today.month)] = {}
            month_base = year_base[str(self.today.month)]

        try:
            day_base = month_base[str(self.today.day)]
        except:
            month_base[str(self.today.day)] = {}
            day_base = month_base[str(self.today.day)]
        try:
            day_base["earn"] += self.earn_money.get()
        except:
            day_base["earn"] = 0
        try:
            day_base["pay"] += self.pay_money.get()
        except:
            day_base["pay"] = 0

        day_base["note"] = "Xin chào! hôm nay tôi vẫn vô dụng chưa làm được gì cả."

        month_base[str(self.today.day)] = day_base
        year_base[str(self.today.month)] = month_base
        self.data_base[str(self.today.year)] = year_base


    def insert_database(self):
        data_plan_block = []
        data_plan_interest = []
        data_plan_lost = []
        total_lost = 5000
        salary = 8000
        ratio = "50-30-10-10"
        ratio = ratio.split("-")
        print(ratio)
        for i in range(len(ratio)):
            if total_lost>0:
                if salary*int(ratio[i])/100 < total_lost:
                    data_plan_lost.append(salary*int(ratio[i])/100)
                else:
                    data_plan_lost.append(total_lost)
                total_lost = total_lost - salary*int(ratio[i])/100
                
            else:
                data_plan_lost.append(0)

            data_plan_block.append(f"Block {i}[{ratio[i]}]")
            data_plan_interest.append(salary*int(ratio[i])/100)
        
        self.data_plan["Blocks"] = data_plan_block
        self.data_plan["Money"] = data_plan_interest
        self.data_plan["Lost"] = data_plan_lost
        self.data_plan["Interest"] = [data_plan_interest[i] - data_plan_lost[i] for i in range(len(data_plan_interest))]

        self.data_plan = pd.DataFrame(data=self.data_plan)
        print(self.data_plan)

    def create_dataframe(self):
        column = {}
        date = "23-2-2021"
        date_ = date.split("-")
        for k in self.data_base[date_[2]][date_[1]]:
            
            for l in self.data_base[date_[2]][date_[1]][k]:
                data_in = self.data_base[date_[2]][date_[1]][k]
                try:
                    column[str(l)].append(data_in[str(l)])
                except:
                    column[str(l)] = []
                    column[str(l)].append(data_in[str(l)])
            try:
                column["date"].append(k)
            except:
                column["date"] = []
                column["date"].append(k)

        self.data_frame = pd.DataFrame(data=column)