import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
import json

def init_gui():
    root = tk.Tk()
    return root



def get_photo():
    url = 'https://randomfox.ca/floof/'
    response = requests.get(url)
    result = json.loads(response.text)
    value = requests.get(f'{result['image']}')
    pil_image = Image.open(BytesIO(value.content))
    image = ImageTk.PhotoImage(pil_image)
    label.config(image=image)
    label.image = image


def init_input(fr_input):
    button = tk.Button(fr_input, text='Генерировать', command= lambda: get_photo())
    button.pack(side=tk.TOP)


def init_frames(root):
    fr_input = tk.Frame(root)
    fr_input.pack()
    return fr_input

if __name__ == '__main__':
    root = init_gui()
    root.geometry('880x880')
    fr_input = init_frames(root)
    label = tk.Label(root)
    label.pack()
    init_input(fr_input)
    root.mainloop()