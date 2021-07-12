from tkinter import *
from ctypes import windll

from BlurWindow.blurWindow import blur

root = Tk()
root.config(bg='green')

root.wm_attributes("-transparent", 'green')
root.geometry('500x400')

root.update()

hWnd = windll.user32.GetForegroundWindow()
blur(hWnd)



def color(hex):
    hWnd = windll.user32.GetForegroundWindow()
    blur(hWnd,hexColor=hex)
    

e = Entry(width=9)
e.insert(0,'#12121240')

e.pack()
b = Button(text='Apply',command=lambda:[color(e.get())])
b.pack()


root.mainloop()



