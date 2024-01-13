import customtkinter
from tkinter import filedialog as fd
from chapter.main_window.audio.audio_process import choose_file_audio, list_file_in_folder
from customtkinter.windows.CtkListbox import CTkListbox
import os
import pygame

class gui_audio(customtkinter.CTk):
    def __init__(self, gui):
        super().__init__()

        pygame.init()
        pygame.mixer.init()
        self.dirname = ''
        self.dirsave = ''
        self.song_list = []
        self.audio_current = ''
        self.size_audio = 0
        self.on_of = False
        self.path_audio = ''
        self.ui = gui
        self.chap = 0

        self.config_grid(self.ui)
        self.frame_audio = customtkinter.CTkFrame(self.ui, corner_radius=10)
        self.frame_audio.grid(row=0, column=0, columnspan = 4, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.config_grid(self.frame_audio)

        # self.ui.grid_columnconfigure((1, 4, 2), weight=1)
        self.frame_list = customtkinter.CTkFrame(self.ui, width=100, corner_radius=10)
        self.frame_list.grid(row=0, column=4, rowspan=4, padx=(0, 20), pady=(20, 0), sticky="nsew")
        self.config_grid(self.frame_list)
        self.listbox = CTkListbox(self.frame_list, command=self.show_value)
        self.listbox.pack(fill="both", expand=True, padx=10, pady=10)
        self.listbox.rowconfigure(0, weight=1)

        #phần văn bản của app
        self.frame_text = customtkinter.CTkFrame(self.ui, corner_radius=5)
        self.frame_text.grid(row=1, column=0, columnspan = 4, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.config_grid(self.frame_text)
        self.textbox = customtkinter.CTkTextbox(self.frame_text)
        self.textbox.grid(row=1, column=0, columnspan = 5, rowspan = 3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.textbox.insert('0.0', 'toilalinh03superbot')

        self.name_audio_frame = customtkinter.CTkFrame(self.frame_audio)
        self.name_audio_frame.grid(row=0, column=1, columnspan = 4,rowspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.name_audio_frame.grid_columnconfigure(2, weight=1)
        self.name_audio_frame.grid_rowconfigure(2, weight=1)
        self.label_audio = customtkinter.CTkLabel(master=self.name_audio_frame, text="Name audio")
        self.label_audio.grid(row=0, column=0, padx=(10, 10), pady=(10, 5), sticky="")
        self.slider_2 = customtkinter.CTkSlider(self.name_audio_frame,from_=0, height=100, to=100, number_of_steps=100, orientation="vertical", command=self.set_vol)
        self.slider_2.grid(row=0, column=4, rowspan=1, padx=(10, 10), pady=(0, 0), sticky="ns")
        # self.config_grid(self.name_audio_frame)


        self.slider_progressbar_frame = customtkinter.CTkFrame(self.name_audio_frame, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=0, columnspan = 4, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(4, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        # self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        # self.progressbar_2.grid(row=1, column=0, padx=(10, 10), pady=(0, 0), sticky="ew")

        self.input_button_back = customtkinter.CTkButton(self.slider_progressbar_frame,width=50, text="<", command=self.opendir)
        self.input_button_back.grid(row=0, column=0, padx=(10, 10), pady=(0, 0))
        self.input_button_next = customtkinter.CTkButton(self.slider_progressbar_frame,width=50, text=">", command=self.create_list)
        self.input_button_next.grid(row=0, column=2, padx=(10, 10), pady=(0, 0))
        self.input_button_play = customtkinter.CTkButton(self.slider_progressbar_frame,width=50, text="Play", command=self.play_audio)
        self.input_button_play.grid(row=0, column=1, padx=(10, 10), pady=(0, 0))
        self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=100, number_of_steps=100, command=self.set_pos)
        self.slider_1.grid(row=0, column=3, columnspan = 4, padx=(10, 10), pady=(0, 0), sticky="ew")
        self.slider_progressbar_frame.bind("<KeyPress>", self.on_key_press)




        self.button_frame_1 = customtkinter.CTkFrame(self.frame_audio)
        self.button_frame_1.grid(row=1, column=1, columnspan = 4, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.button_frame_1.grid_columnconfigure(2, weight=1)
        self.button_frame_1.grid_rowconfigure(2, weight=1)

        self.combobox_3 = customtkinter.CTkComboBox(self.button_frame_1, width=300, values=['...'])
        self.combobox_3.grid(row=0, column=0, rowspan = 1, padx=(10, 10), pady=(10, 10))
        self.input_button_3 = customtkinter.CTkButton(self.button_frame_1, text="Choose", command=self.opendir)
        self.input_button_3.grid(row=0, column=1,  padx=(10, 10), pady=(10,10))
        self.combobox_4 = customtkinter.CTkComboBox(self.button_frame_1, width=300, values=['...'])
        self.combobox_4.grid(row=1, column=0,  padx=(10, 10), pady=(10, 10))
        self.input_button_4 = customtkinter.CTkButton(self.button_frame_1, text="Save", command=self.opensave)
        self.input_button_4.grid(row=1, column=1, padx=(10, 10), pady=(10,10))


    #     self.button_frame = customtkinter.CTkFrame(self.audio_frame)
    #     self.button_frame.grid(row=2, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
    #     self.input_button_next = customtkinter.CTkButton(self.button_frame, text="<", command=self.opendir)
    #     self.input_button_next.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))
    #     self.input_button_back = customtkinter.CTkButton(self.button_frame, text=">", command=self.create_list)
    #     self.input_button_back.grid(row=2, column=3, padx=(0, 0), pady=(0, 0))
    #     self.input_button_play = customtkinter.CTkButton(self.button_frame, text="Play", command=self.play_audio)
    #     self.input_button_play.grid(row=2, column=1, padx=(0, 0), pady=(0, 0))

    #     self.slider_progressbar_frame = customtkinter.CTkFrame(self.audio_frame, fg_color="transparent")
    #     self.slider_progressbar_frame.grid(row=3, column=1, padx=(0, 0), pady=(20, 0), sticky="nsew")
    #     self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
    #     self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
    #     self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
    #     self.progressbar_2.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="ew")
    #     self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=100, number_of_steps=100, command=self.set_pos)
    #     self.slider_1.grid(row=1, column=0, padx=(0, 0), pady=(5, 0), sticky="ew")

    #     self.slider_2 = customtkinter.CTkSlider(self.audio_frame,from_=0, to=100, number_of_steps=100, orientation="vertical", command=self.set_vol)
    #     self.slider_2.grid(row=0, column=2, rowspan=5, padx=(0, 0), pady=(0, 0), sticky="ns")
    #     self.progressbar_3 = customtkinter.CTkProgressBar(self.audio_frame, orientation="vertical")
    #     self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(30, 0), pady=(0, 0), sticky="ns")
        

    #     self.radiobutton_frame = customtkinter.CTkFrame(gui)
    #     self.radiobutton_frame.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
    
    #     self.listbox = CTkListbox(self.radiobutton_frame, command=self.show_value)
    #     self.listbox.pack(fill="both", expand=True, padx=10, pady=10)
    #     # self.listbox.rowconfigure(0, weight=1)

    #     self.input_button_play.configure(state = 'disabled')
    #     self.textbox = customtkinter.CTkTextbox(self.audio_funct, width=500)
    #     self.textbox.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
    #     self.textbox.insert('0.0', 'toilalinh03superbot')




    def config_grid(self, gui):
        gui.grid_columnconfigure(1, weight=1)
        gui.grid_columnconfigure((3, 4), weight=1)
        gui.grid_rowconfigure((0, 1, 2), weight=1)

    def opendir(self):
        self.dirname = fd.askdirectory()
        # print(self.filename)
        self.combobox_3.set(str(self.dirname))
        self.song_list = list_file_in_folder(self.dirname)
        self.input_button_play.configure(state = 'normal')
        self.add_listbox(self.song_list, 0, len(self.song_list)//50)
        # self.play_song_init = Play_audio(self.song_list)

    def create_list(self):
        self.chap += 1
        self.listbox.delete(0, len(self.song_list)//50)
        self.add_listbox(self.song_list, self.chap*len(self.song_list)//50, (self.chap+1)*len(self.song_list)//50)
        # print("###############", self.chap)
        if self.chap > 50:
            self.add_listbox(self.song_list, (self.chap+1)*len(self.song_list)//50, len(self.song_list))

    def back_list(self):
        self.chap -= 1
        if self.chap < 0:
            self.chap = 0
            return
        self.listbox.delete(0, len(self.song_list)//50)
        self.add_listbox(self.song_list, self.chap*len(self.song_list)//50, (self.chap+1)*len(self.song_list)//50)

    def add_listbox(self, list_f, st, en):
        if len(list_f) > 0:
            for i in range(en-st):
                self.listbox.insert(i, list_f[st+i])
        print("Song list none")

    def opensave(self):
        self.dirsave = fd.askdirectory()
        self.combobox_4.set(str(self.dirname))

    def show_value(self, selected_option):
        self.audio_current = selected_option
        self.label_audio.configure(text=self.audio_current)
        self.path_audio = os.path.join(self.dirname, self.audio_current)
        text_, path_lab = self.get_label_path(self.audio_current)
        text = self.textbox.get("0.0", "end")
        if 'toilalinh03superbot' in text:
            self.path_labels_current = path_lab
            # print('không được lưu')
        else :
            # print("Save file complete!", self.path_labels_current)
            with open(self.path_labels_current, 'w', encoding='utf-8') as file:
                file.write(text)
                # file.close()
            self.path_labels_current = path_lab
        # print('@@@@@@@@@@@@', text_)
        self.textbox.delete("0.0", "end")
        self.textbox.insert('0.0', text_)
        self.play()
        self.update_slider()
        self.on_of = False
        self.input_button_play.configure(text='Pause')



    #     # print(self.path_audio)
    
    def get_label_path(self, name):
        name_file = name
        name_file = name_file.replace('.wav', '.txt')
        path_label = os.path.join(self.dirsave, name_file)
        # print("###################",path_label)
        with open(path_label, encoding='utf-8') as f:
            data=  f.read()
            # print(data)
            # f.close()
        return data, path_label

    def on_key_press(event):
        key = event.keysym
        print(f"Key pressed: {key}")

    def play_audio(self):
        # print(self.on_of)
        if self.on_of :
            self.on_of = False
            # self.on_of = True
            pygame.mixer.music.unpause()
            self.input_button_play.configure(text='Pause')
            self.play()

        elif not self.on_of:
            self.on_of = True
            # self.on_of = False

            self.input_button_play.configure(text='Play')
            pygame.mixer.music.pause()
            
    def play(self):
        # print(self.path_audio)
        pygame.mixer.music.load(self.path_audio)
        a = pygame.mixer.Sound(self.path_audio)
        self.size_audio = a.get_length()
        # print(self.size_audio)
        pygame.mixer.music.play()
    
    def set_vol(self, val):
        volume = int(val) / 100
        # self.progressbar_3.set(volume)
        # print(volume)
        pygame.mixer.music.set_volume(volume)
    
    def set_pos(self, val):
        # print(self.size_audio)
        # print("length",a.get_length())
        pos = int(float(val) / 100 * self.size_audio)
        # self.progressbar_2.set(pos)
        #  int(val) * self.size_audio / 100
        pygame.mixer.music.set_pos(pos)

    def update_slider(self):
        if not self.on_of and self.size_audio!=0:
            current_position = pygame.mixer.music.get_pos() / 1000.0  # Chuyển đổi miliseconds sang seconds
            progress_percentage = int((current_position / self.size_audio) * 100)
            # print(progress_percentage)
            if progress_percentage > 50:
                self.on_of = True
                # progress_percentage = 100
                self.input_button_play.configure(text='Play')

            # self.progressbar_2.set(progress_percentage)
            self.slider_1.set(progress_percentage)
        self.ui.after(1000, self.update_slider)
    
