from gtts import gTTS
from tkinter import*
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog
from langdetect import detect

root = Tk()
root.title("Синтезатор речи")
root.geometry("185x50")
root.resizable(width=0, height=0)

entry = Entry( width=30,relief = 'flat')
entry.grid(row=5,column=0, padx=0, pady=1)

button1 = Button(text="Сохранить",relief = 'flat',command=lambda: se())
button1.grid(row=6, column=0,sticky="e")

def se():
    tts = gTTS(entry.get(), lang=detect(entry.get()))
    tts.save(filedialog.asksaveasfilename(defaultextension=".mp3",filetypes=(("Audio files", "*.mp3"),
                   ("All files", "*.*"))))
             
root.mainloop()
