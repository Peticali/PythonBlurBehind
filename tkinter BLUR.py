from tkinter import *
import ctypes

from BlurWindow.blurWindow import blur

root = Tk()
root.config(bg='green')

root.wm_attributes("-transparent", 'green')
root.geometry('500x400')
root.update()

global HWND
HWND = ctypes.windll.user32.GetForegroundWindow()
blur(HWND,Acrylic=True)

def color(hex):
    blur(HWND,hexColor=hex)

e = Entry(width=9)
e.insert(0,'#12121240')

e.pack()
b = Button(text='Apply',command=lambda:[color(e.get())])
b.pack()


root.mainloop()



