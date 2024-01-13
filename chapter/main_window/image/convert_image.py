from PIL import Image
from pydub import AudioSegment

import os

def image2ico(path_input, path_output, size_output=(256,256), name_file=None):
    if name_file==None:
        encode_image = ['.png', '.jpg']
        for i in encode_image:
            name_file = path_input.split('/')[-1].replace(i,'')
    name_file = name_file + '.ico'
    print(name_file)
    logo = Image.open(path_input)
    logo.save(os.path.join(path_output, name_file), format='ICO', sizes=[size_output])

def video2wav(path_input, path_output, name_file):
    sound = AudioSegment.from_mp3(path_input)
    sound.export(os.path.join(path_output, 'result_image.wav'), format="wav")

image2ico("C:/Users/Hero/Downloads/logodbot04.png-removebg-preview.png", 'C:/Users/Hero/OneDrive/Máy tính/Dbot09')