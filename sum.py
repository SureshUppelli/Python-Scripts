from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")
#lbl = Label(window, text="Hello this my first GUI Program", font=("Arial Bold", 50))
lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)
btn = Button(window, text="Click Me")

btn.grid(column=1, row=0)
window.geometry('350x200')

window.mainloop()