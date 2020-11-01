from tkinter import *

lang = ["Python", "C++", "Java"]


def fun():
    for i in range(3):
        if var1.get() - 1 == i:
            label1.configure(text=lang[i])


window = Tk()
window.geometry("720x560")
var1 = IntVar()

label1 = Label(window, text="Selected Language:")
radios = [
    Radiobutton(
        window,
        text=lang[i],
        variable=var1,
        value=i + 1,
        command=fun,
    )
    for i in range(3)
]

label1.pack()
for rb in radios:
    rb.pack()

window.mainloop()