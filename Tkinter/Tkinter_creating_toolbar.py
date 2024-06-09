from tkinter import *
def donothing():
    print("ok")
    

root=Tk()

menu=Menu(root)
root.config(menu=menu)
subMenu=Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Folder..", command=donothing)
subMenu.add_command(label="New..", command=donothing)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=donothing)

editMenu=Menu(menu)
menu.add_cascade(label="Exit", menu=editMenu)
editMenu.add_command(label="Redo", command=donothing)

#.........toolbar.......
toolbar=Frame(root, bg="blue")

insertButt=Button(toolbar, text="insert image", command=donothing)
insertButt.pack(side=LEFT, padx=2,pady=2)
printButt=Button(toolbar, text="print", command=donothing)
printButt.pack(side=LEFT, padx=2,pady=2)
toolbar.pack(side=TOP,fill=X)
root.mainloop()
