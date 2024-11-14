from tkinter import *
from  tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

t = 0
music = False
text = ' '

def set():
    global t
    global text
    rem = sd.askstring('Время напоминания',
                       'Введите время напоминания ЧЧ:ММ в формате 24 часа')
    if rem:
        try:
            hour = int(rem.split(':')[0])
            minute = int(rem.split(':')[1])
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour = hour, minute = minute, second = 0)
            print(dt)
            t = dt.timestamp()
            print(t)
            text = sd.askstring('Текст напоминания',
                                'Введите текст напоминания')
            label.config(text = f'Напоминание: {hour:02}:{minute:02} "{text}"')
        except Exception as e:
            mb.showerror('Ошибка!', f'Произошла ошибка {e}')

def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            popup_window()
            t = 0
    window.after(10000, check)

def play_snd():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load('weely.mp3')
    pygame.mixer.music.play()

def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    label.config(text = 'Установить новое напоминание')

def popup_window():
    global text
    window = Tk()
    window.title('Напоминание')
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w_2 = w // 2
    h_2 = h // 2
    window.geometry(f'500x300+{w_2 - 250}+{h_2 - 150}')
    label = Label(window, text = f'Напоминание:\n"{text}"', font = ('Arial', 24))
    label.pack(pady = 30)

window = Tk()
window.title('Напоминание')
label = Label(text = 'Установите напоминание', font = ('Arial', 14))
label.pack(pady = 10)
set_button = Button(text = 'Установить напоминание', command = set)
set_button.pack(pady = 10)

stop_button = Button(text = 'Остановить музыку', command = stop_music)
stop_button.pack(pady = 10)

check()

window.mainloop()
