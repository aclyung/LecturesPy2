from tkinter import *
from tkinter.simpledialog import *

window = Tk()
window.geometry("400x100")

label1 = Label(window, text="입력값", fg="magenta", font=("D2coding", 20))
label1.pack()
value = askinteger("Dice number", "Please enter number",
                   minvalue=1, maxvalue=6)
label1.configure(text=str(value))

window.mainloop()
