from tkinter import *
import tkinter.messagebox

master = Tk()
e = Entry(master)
e.pack()

e.focus_set()

def callback():
    
    print(e.get()) # This is the text you may want to use later

b = Button(master, text = "OK", width = 10, command = callback)
b.pack()

#mainloop()

#root=Tk()
tkinter.messagebox.showinfo("window title", "this is a window message box")

answer=tkinter.messagebox.askquestion("Question 1", "do you like funny face?")
if answer=="yes":
    print(b.pack())
#root.mainloop()
mainloop()
