from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("720x560")
button = Button(
    window,
    text="Exit",
    font=("D2Coding", 20),
    fg="DodgerBlue2",
    command=(lambda: messagebox.showinfo("Foo", "hello")),
)
button.pack()
window.mainloop()
