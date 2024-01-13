import os
import pygame
import tkinter as tkr


def list_file_in_folder(filename):
    file_inpaths = os.listdir(filename)
    return choose_file_audio(file_inpaths)


def choose_file_audio(list_files):
    list_wav = []
    for file in list_files:
        if '.wav' in file:
            list_wav.append(file)
    return list_wav

class Play_audio():

    def __init__(self, play_lists, name=''):
        self.size_audio = 0
        pygame.init()
        pygame.mixer.init()
        self.play_list = play_lists
        self.on_of = True
        self.audio_current = name

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def set_vol(self, val):
        volume = int(val) / 100
        pygame.mixer.music.set_volume(volume)
    def set_pos(self, val):
        print(self.size_audio)
        pos = int(val) * self.size_audio / 100
        pygame.mixer.music.set_pos(pos)

    def play(self):
        # global size_audio
        path = os.path.join(self.play_list, self.audio_current)
        print(path)
        # try:
        # path = self.play_list.get(tkr.ACTIVE)
        a = pygame.mixer.Sound(path)
        self.size_audio = a.get_length()
        print(a, self.size_audio)
        print(self.on_of)
        if self.on_of == True:
            self.unpause()
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
            self.on_of == False
        else:
            self.on_of == True
            self.pause()
        # except:
        #     print('Error')