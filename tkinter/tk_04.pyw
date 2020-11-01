from tkinter import *
import os

file_path = os.path.dirname(os.path.abspath(__file__))

window = Tk()
image = PhotoImage(file=file_path + "/res/GIF/dog.gif")
image2 = PhotoImage(file=file_path + "/res/GIF/dog3.gif")
# PhotoImage(
#     file="C:\\Users\\KGITBank\\Documents\\Workspace\\Python\\Lecturespy2\\Tkinter\\res\\GIF\\cat.gif"
# )
label1 = Label(window, image=image)
label2 = Label(window, image=image2)
button = Button(window, text="Exit", command=lambda: exit(0))
button.pack()
label1.pack(side=LEFT)
label2.pack()
window.mainloop()