from gtts import gTTS
import tkinter
from tkinter import*
import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog
from langdetect import detect


root = Tk()
root.title("Синтезатор речи")
root.resizable(width=0, height=0)
m = Menu(root)
root.config(menu=m) 

m.add_command(label='Открыть',command=lambda: o())
m.add_command(label='Переобразовать',command=lambda: se())

entry = Text( width=100,relief = 'flat')
entry.grid(row=5,column=0, padx=0, pady=1)

scrollb = Scrollbar(root, command=entry.yview,relief = 'flat')
scrollb.grid(row=5, column=4, sticky='nsew')
entry.configure(yscrollcommand=scrollb.set)

def o():
    file_name = filedialog.askopenfilename()
    f = open(file_name)
    s = f.read()
    entry.insert(1.0, s)
    f.close()

def s():
    tts = gTTS(entry.get('1.0',END), lang=detect(entry.get('1.0',END)))
    tts.save(filedialog.asksaveasfilename(defaultextension=".mp3",filetypes=(("Audio files", "*.mp3"),
                   ("All files", "*.*"))))
             
root.mainloop() 
