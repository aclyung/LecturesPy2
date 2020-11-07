from tkinter import *
import os

window = Tk()
imgdir = os.path.dirname(os.path.abspath(__file__)) + "/res/GIF/"

photo = PhotoImage(file=imgdir + "/dog5.gif")
label1 = Label(window, image=photo)

label1.pack()
window.mainloop()
