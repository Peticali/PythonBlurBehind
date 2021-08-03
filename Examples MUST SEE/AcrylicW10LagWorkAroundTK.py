#https://github.com/sourcechord/FluentWPF/issues/42#issuecomment-873615119 idea
from tkinter import *
import ctypes
from BlurWindow.blurWindow import blur,Win7Blur,GlobalBlur

root = Tk()
root.config(bg='green')

root.wm_attributes("-transparent", 'green')
root.geometry('500x400')
root.update()

HWND = ctypes.windll.user32.GetForegroundWindow()

GlobalBlur(HWND,Acrylic=True) #Enable Acrylic

global ACRYLIC_ENABLED
ACRYLIC_ENABLED = True

global DRAG
DRAG = False

def dragging(event):
    global DRAG
    if event.widget is root: #if is event Configure of root (Drag,Resize)
        if DRAG == False:#If Drag is disabled (set by stop_drag)
            GlobalBlur(HWND,Acrylic=False)
        else:
            root.after_cancel(DRAG) #cancel task \/ (is dragging)
        DRAG = root.after(200, stop_drag) #execute stop_drag after 200ms

def stop_drag():
    global DRAG
    DRAG = False
    GlobalBlur(HWND,Acrylic=True) 

root.bind('<Configure>', dragging)

root.mainloop()