# from tkinter import *
# from tkinter import messagebox
# import os
# import random

# window = Tk()
# imgdir = os.path.dirname(os.path.abspath(__file__)) + "/res/GIF/"
# window.geometry("210x210")
# window.title("Foo")
# ftype = ".gif"
# framelist = [
#     "froyo",
#     "gingerbread",
#     "honeycomb",
#     "icecream",
#     "jellybean",
#     "kitkat",
#     "lollipop",
#     "marshmallow",
#     "nougat",
# ]
# random.shuffle(framelist)


# def mbox(i):
#     messagebox.showinfo("photo", i)


# images = [PhotoImage(file=imgdir + v + ftype) for v in framelist]
# var = IntVar()
# btn = [
#     Button(
#         image=i,
#         command=lambda: mbox(str(var.get())),
#     )
#     for i, k in zip(images, range(9))
# ]


# num, x, y = 0, 0, 0
# for k in btn:
#     if num >= 3 and num % 3 == 0:
#         x = 0
#         y += 70
#     k.place(x=x, y=y)
#     x += 70
#     num += 1

# window.mainloop()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({"a": [4, 5, 6], "b": [7, 8, 9], "c": [10, 11, 12]}, index=[1, 2, 3])

x = df["a"]

y = df.loc[2]
plt.plot(x, y)
plt.show()
