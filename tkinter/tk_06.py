from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showerror, showinfo

window = Tk()
window.geometry("720x560")


def fun():
    if chk.get() == 0:
        messagebox.showinfo("Info", "Button Not Checked")
    else:
        messagebox.showinfo("Info", "Button Checked")


chk = IntVar()
check_button = Checkbutton(
    window, text="FOO", variable=chk, command=lambda: print(chk.get())
)
button = Button(window, text="check", font=("D2Coding", 16), command=fun)
check_button.pack()
button.pack()
window.mainloop()