from tkinter import *
import ctypes

from BlurWindow.blurWindow import blur,Win7Blur

root = Tk()
root.config(bg='green')

root.wm_attributes("-transparent", 'green')
root.geometry('500x400')
root.update()

global HWND
HWND = ctypes.windll.user32.GetForegroundWindow()
blur(HWND)


def color(hex):
    blur(HWND,hexColor=hex)

def color2(hex):
    blur(HWND,hexColor=hex,Acrylic=True)

def Win7():
    Win7Blur(HWND)


e = Entry(width=9)
e.insert(0,'#12121240')

e.pack()
b = Button(text='Apply',command=lambda:[color(e.get())])
b.pack()
b = Button(text='ApplyAcrylic',command=lambda:[color2(e.get())])
b.pack()
b = Button(text='Win7Blur',command=Win7)
b.pack()


root.mainloop()