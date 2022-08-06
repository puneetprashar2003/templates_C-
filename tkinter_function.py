import tkinter
import turtle
window=tkinter.Tk()

window.title("my first gui program")
window.minsize(width=500,height=300)
my_label=tkinter.Label(text="hlo guys",font=("Arial",18,"bold"))
my_label.pack(side="left")
window.mainloop()