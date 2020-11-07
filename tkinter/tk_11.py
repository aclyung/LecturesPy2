from tkinter import *
from tkinter import messagebox
import os


def fun():
    messagebox.showinfo("Doggy", "Puppy ")


imgdir = os.path.dirname(os.path.abspath(__file__)) + "/res/GIF/"

window = Tk()
photo = PhotoImage(file=imgdir+"dog7.gif")
btn = Button(window, image=photo, command=fun)
btn.pack()

window.mainloop()
