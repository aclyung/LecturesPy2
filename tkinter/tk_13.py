from tkinter import *
from tkinter import messagebox


def key_event(event):
    messagebox.showinfo("Keyboard Event", chr(event.keycode)+" button clicked")


window = Tk()

window.bind("<Key>", key_event)
window.mainloop()
