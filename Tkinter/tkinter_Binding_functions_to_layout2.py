from tkinter import *
root=Tk()
def printName():
    print("me name is Ejaz")
button_1=Button(root, text="Print my name", command=printName)
button_1.pack()
root.mainloop()
