from tkinter import *
from tkinter.messagebox import showinfo

window = Tk()
window.title("FOO")
window.geometry("300x140")
var = IntVar()
btn = [
    Button(
        text="버튼" + str(i),
        width=10,
        font="D2Coding",
        fg="Coral",
        background="DodgerBlue",
    )
    for i in range(1, 10)
]
num, x, y = 0, 0, 0
for k in btn:
    if num >= 3 and num % 3 == 0:
        x = 0
        y += 50
    k.place(x=x, y=y)
    x += 100
    num += 1

# for v in range(3):
#     for i in range(3):
#         btn[num].place(x=x, y=y)
#         num += 1
#         x += 100
#     x = 0
#     y += 50


window.mainloop()
