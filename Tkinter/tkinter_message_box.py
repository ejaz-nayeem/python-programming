from tkinter import *
import tkinter.messagebox

root=Tk()
tkinter.messagebox.showinfo("window title", "this is a window message box")

answer=tkinter.messagebox.askquestion("Question 1", "do you like funny face?")
if answer=="yes":
    print("B===D=")
root.mainloop()
