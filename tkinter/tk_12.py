from tkinter import *
from tkinter import messagebox


def click_event(event):
    txt = ""
    if event.num == 1:
        txt += "Left Btn "

    elif event.num == 3:
        txt += "Right Btn "
    txt += str(event.x)+", "+str(event.y)
    label1.configure(text=txt)


window = Tk()
window.geometry("400x400")

label1 = Label(window, text="Current Cursor location here", fg="Coral")

window.bind("<Button>", click_event)
label1.pack()

window.mainloop()
