import customtkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter
import seaborn as sns
from datetime import date
import calendar
import pandas as pd
from tkinter import ttk
import json
import logging
logger = logging.getLogger("__BoxC__")

class gui_vizualize(customtkinter.CTk):
    def __init__(self, gui):
        super().__init__()
        self.data_frame = []
        self.data_plan = {}
        self.data_base = {}
        self.setup = True
        # sns.set()
        self.today = date.today()
        _, self.days = calendar.monthrange(self.today.year, self.today.month)
        self.except_ = False
        self.money = tkinter.StringVar()
        self.money.set("0"*9+".0")

        # ax.set_xticklabels(ax.get_xticklabels(), rotation=60, horizontalalignment="center")
        self.ui = gui
        self.ui.grid_columnconfigure(2, weight=1)
        self.ui.grid_rowconfigure(2, weight=1)

        self.pay = customtkinter.CTkEntry(self.ui, placeholder_text="CTkEntry")
        self.pay.grid(row=3, column=0, columnspan=5, padx=(20, 20), pady=(20, 20), sticky="nsew")

        ###---------###
        self.frame_insert = customtkinter.CTkFrame(self.ui, corner_radius=10,)
        self.frame_insert.grid(row=0, column=0, columnspan = 1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        ### block 0 ###

        self._optionemenu = customtkinter.CTkOptionMenu(self.frame_insert, values=["Total", "Interest", "Expenses"], command=self.control_graph)
        self._optionemenu.grid(row=0, column=0, padx=(20, 20), pady=(20, 0))
        self.day_current = customtkinter.CTkEntry(self.frame_insert, placeholder_text="CTkEntry")
        self.day_current.grid(row=0, column=1, columnspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.total_money_label = customtkinter.CTkLabel(self.frame_insert, text="Total money:", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.total_money_label.grid(row=1, column=0, columnspan = 1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.total_money = customtkinter.CTkEntry(self.frame_insert, textvariable=self.money, font=customtkinter.CTkFont(size=20, weight="bold"), state="readonly")
        self.total_money.grid(row=1, column=1, columnspan = 1, padx=(20, 20), pady=(20, 0), sticky="nsew")


        self.pay_money_label = customtkinter.CTkLabel(self.frame_insert, text="Pay money:", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.pay_money_label.grid(row=2, column=0, columnspan = 1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.pay_money = customtkinter.CTkEntry(self.frame_insert, placeholder_text="Nhập số tiền mất hôm nay", font=customtkinter.CTkFont(size=10, weight="normal"))
        self.pay_money.grid(row=2, column=1, columnspan = 1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.pay_money.bind("<Return>", self.on_enter)

        self.earn_money_label = customtkinter.CTkLabel(self.frame_insert, text="Earn money:", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.earn_money_label.grid(row=3, column=0, columnspan = 1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.earn_money = customtkinter.CTkEntry(self.frame_insert, placeholder_text="Nhập số tiền kiếm được hôm nay", font=customtkinter.CTkFont(size=10, weight="normal"))
        self.earn_money.grid(row=3, column=1, columnspan = 1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.earn_money.bind("<Return>", self.update_data_today)
        
        #####################
        ###---------###
        self.frame_grap = customtkinter.CTkFrame(self.ui, corner_radius=10, width=200)
        self.frame_grap.grid(row=0, column=1, columnspan = 2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.frame_grap.grid_columnconfigure(2, weight=1)
        self.frame_grap.grid_rowconfigure(2, weight=1)
        ### block 1 ###
        self.frame_control = customtkinter.CTkFrame(self.ui, corner_radius=10,)
        self.frame_control.grid(row=1, column=0, columnspan = 1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        

        self.plan_save_money = customtkinter.CTkFrame(self.ui, corner_radius=10, width=200)
        self.plan_save_money.grid(row=1, column=2, columnspan = 2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.plan_save_money.grid_columnconfigure(2, weight=1)
        self.plan_save_money.grid_rowconfigure(2, weight=1)

        self.extra_save_money = customtkinter.CTkFrame(self.ui, corner_radius=10, width=200)
        self.extra_save_money.grid(row=2, column=0, columnspan = 5, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.extra_save_money.grid_columnconfigure(2, weight=1)
        self.extra_save_money.grid_rowconfigure(2, weight=1)
        try:
            with open("chapter/main_window/database/data_base.json", 'r', encoding='utf-8') as json_file:
                self.data_base = json.load(json_file)
        except Exception as e:
            self.except_ = True
            logger.error('Không có dữ liệu trong file json', e)
        with open("chapter/main_window/database/config.json", 'r', encoding='utf-8') as json_file:
            self.data_config = json.load(json_file)

        self.set_up_database()
        self.create_dataframe()
        self.insert_database()
        self.visual_graph()
        self.visual_table()

    def on_enter(self,event):
        # Hàm xử lý khi nhấn Enter
        self.earn_money.focus_set()

    def control_graph(self, value):
        # "Total", "Interest", "Expenses"
        if "Total" in value:
            print("Total money:")            
            message = str(self.data_config["salary"])
        elif "Interest" in value:
            print("Interest money:")
            message = str(self.data_config["salary"]-self.data_config["total_lost"])    
        elif "Expenses" in value:
            print("Expenses money:")            
            message = str(self.data_config["total_lost"])
        self.money.set('0'*(11-len(message))+message)
        self.total_money.configure(textvariable=self.money)
        

    def visual_graph(self):
        self.frame_grap.destroy()
        self.frame_grap = customtkinter.CTkFrame(self.ui, corner_radius=10, width=200)
        self.frame_grap.grid(row=0, column=2, columnspan = 2, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.plan_save_money.destroy()
        self.plan_save_money = customtkinter.CTkFrame(self.ui, corner_radius=10, width=200)
        self.plan_save_money.grid(row=1, column=2, columnspan = 2, padx=(20, 20), pady=(20, 0), sticky="nsew")

        figure_top = Figure(figsize=(7, 3))
        figure_mid = Figure(figsize=(7, 3))
        ax_top = figure_top.subplots()
        ax_mid = figure_mid.subplots()

        ax=sns.barplot(self.data_frame, x="date", y="earn", ax=ax_top, errorbar=None, label = "pay")
        ax.patches[0].set_facecolor('orange')  # Đổi màu cột thứ 2 thành màu cam
        ax_ = ax_top.twinx()
        ax_ = sns.lineplot(x='date', y='pay', data=self.data_frame, marker='o', ax=ax_, color='red', label='earn')
        
        sns.barplot(self.data_plan, x="Blocks", y="Interest", ax=ax_mid, errorbar=None, label = "plan", color='green')
        sns.barplot(self.data_plan, x="Blocks", y="Lost", ax=ax_mid, errorbar=None, label = "plan", color='red',bottom=self.data_plan['Interest'])

        canvas_top = FigureCanvasTkAgg(figure_top, master=self.frame_grap)
        canvas_mid = FigureCanvasTkAgg(figure_mid, master=self.plan_save_money)

        canvas_top.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH,  expand=6)
        canvas_mid.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH,  expand=6)
        
        canvas_top.draw()
        canvas_mid.draw()

        # except:
        #     canvas_top.delete("all")
        #     canvas_mid.delete("all")
        #     self.visual_graph()
            
    def visual_table(self):
        self.extra_save_money.destroy()
        self.extra_save_money = customtkinter.CTkFrame(self.ui, corner_radius=10, width=200)
        self.extra_save_money.grid(row=2, column=0, columnspan = 5, padx=(20, 20), pady=(20, 0), sticky="nsew")
       
        self.tree = ttk.Treeview(self.extra_save_money, columns=list(self.data_plan.columns), show="headings")
        for col in self.data_plan.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)  # Thiết lập độ rộng cột (có thể điều chỉnh)
        for index, row in self.data_plan.iterrows():
            self.tree.insert("", "end", values=tuple(row))
        yscrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=yscrollbar.set)

        # Hiển thị Treeview và Scrollbar
        self.tree.pack(side="left", fill="both", expand=True)
        yscrollbar.pack(side="right", fill="y")
        style = ttk.Style()
        style.theme_use("clam")
        style.map("Treeview")

    def create_database(self):
        data_base = {}
        year_base = {}
        month_base = {}
        day_base = {}
        self.today = date.today()
        _, self.days = calendar.monthrange(self.today.year, self.today.month)
        day_base["earn"] = 0
        day_base["pay"] = 0
        month_base[str(self.today.day)] = day_base
        year_base[str(self.today.month)] = month_base
        data_base[str(self.today.year)] = year_base


    # def create_database(self,data_base):
    def create_dataframe(self):
        column = {}
        # date = "23-2-2021"
        date = f"{self.today.day}-{self.today.month}-{self.today.year}"
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

        # return data_frame
    def set_up_database(self):
        # today = f"{self.today.day}-{self.today.month}-{self.today.year}"
        print("Update data base!")
        if self.today.day-1<1 or self.except_ == True:
            self.setup=False
            for i in range(self.days):
                self.input_date = f"{i+1}-{self.today.month}-{self.today.year}"
                self.update_database()
        # yesterday = f"{self.today.day-1}-{self.today.month}-{self.today.year}"

    def update_data_today(self, event):
        print("Update data today!")
        self.setup == True
        self.update_database()

    def update_database(self):
        try:
            earn_money = float(self.earn_money.get())
            pay_money = float(self.pay_money.get())
        except:
            earn_money = 0
            pay_money = 0

        if self.setup == True:
            date_ = f"{self.today.day}-{self.today.month}-{self.today.year}"
        else:
            date_ = self.input_date
        date_ = date_.split("-")
        print(date_)
        try:
            year_base = self.data_base[date_[2]]
        except:
            self.data_base[date_[2]] = {}
            year_base = self.data_base[date_[2]]

        try:
            month_base = year_base[date_[1]]
        except:
            year_base[date_[1]] = {}
            month_base = year_base[date_[1]]

        try:
            day_base = month_base[date_[0]]
        except:
            month_base[date_[0]] = {}
            day_base = month_base[date_[0]]
        try:
            day_base["earn"] += earn_money
        except:
            day_base["earn"] = 0
            # day_base["earn"] += int(self.earn_money.get())
        try:
            day_base["pay"] += pay_money
        except:
            day_base["pay"] = 0
            # day_base["pay"] += int(self.pay_money.get())


        day_base["note"] = "Xin chào! hôm nay tôi vẫn vô dụng chưa làm được gì cả."

        month_base[date_[0]] = day_base
        year_base[date_[1]] = month_base
        self.data_base[date_[2]] = year_base
        self.data_config["total_lost"] += pay_money
        print(self.data_config)
        with open("chapter/main_window/database/data_base.json", 'w', encoding="utf-8") as json_file:
            json.dump(self.data_base, json_file, ensure_ascii=False)
        with open("chapter/main_window/database/config.json", 'w', encoding="utf-8") as json_file:
            json.dump(self.data_config, json_file, ensure_ascii=False)
        if self.setup==True:
            self.create_dataframe()
            self.insert_database()
            self.visual_graph()
            self.visual_table()

        

    def insert_database(self):
        data_plan_block = []
        data_plan_interest = []
        data_plan_lost = []
        self.ratio = self.data_config["ratio"]
        self.salary=self.data_config["salary"]
        self.total_lost = self.data_config["total_lost"]
        ratio = self.ratio.split("-")
        print(ratio)
        for i in range(len(ratio)):
            if self.total_lost>0:
                if self.salary*int(ratio[i])/100 < self.total_lost:
                    data_plan_lost.append(self.salary*int(ratio[i])/100)
                else:
                    data_plan_lost.append(self.total_lost)
                self.total_lost = self.total_lost - self.salary*int(ratio[i])/100
                
            else:
                data_plan_lost.append(0)

            data_plan_block.append(f"Block {i}[{ratio[i]}]")
            data_plan_interest.append(self.salary*int(ratio[i])/100)
        
        self.data_plan["Blocks"] = data_plan_block
        self.data_plan["Money"] = data_plan_interest
        self.data_plan["Lost"] = data_plan_lost
        self.data_plan["Interest"] = [data_plan_interest[i] - data_plan_lost[i] for i in range(len(data_plan_interest))]

        self.data_plan = pd.DataFrame(data=self.data_plan)
        print(self.data_plan)



