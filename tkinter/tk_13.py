from tkinter import *
from tkinter import messagebox


def menu_btn(str):
    if str == "Exit":
        exit(0)
    else:
        messagebox.showinfo("Menu", str+" Button clicked")


window = Tk()

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="Open File...",
                     command=lambda: menu_btn("Open File..."))
fileMenu.add_command(label="Open Folder...",
                     command=lambda: menu_btn("Open Folder..."))
fileMenu.add_separator()
fileMenu.add_command(label="Save", command=lambda: menu_btn("Save"))
fileMenu.add_command(label="Save as...",
                     command=lambda: menu_btn("Save as..."))
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=lambda: menu_btn("Exit"))

window.mainloop()
