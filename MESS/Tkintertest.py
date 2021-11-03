
from tkinter import *
from tkinter.messagebox import showinfo


def clicked():
    msg = "WHAT THE FUCK DID YOU DO"
    showinfo(title="YOU FUCKING IDIOT", message=msg)


root = Tk()

button = Button(
    master=root,
    text="don't FUCKING press it",
    command=clicked
    )
button.pack(pady=10)

root.mainloop()
