from tkinter import *

mainForm = Tk()

# Form Window
mainForm.title("FOO")
mainForm.geometry("400x400")
mainForm.resizable(width=FALSE, height=FALSE)

# Form Widget
label1 = Label(mainForm, text="Python Language", font=("D2Coding", 20), fg="Black")
label1.pack()

# Window Init
mainForm.mainloop()
