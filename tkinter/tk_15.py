from tkinter import *
from tkinter.filedialog import *

window = Tk()

window.geometry("400x100")
label = Label(window, text="File name")

label.pack()

filename = askopenfilename(parent=window, filetypes=(
    ("gif Files", "*.gif"), ("All types", "*.*")))
label.configure(text=filename)
window.mainloop()
