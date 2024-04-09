
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('300x200')
root.title("check button")

def show_choice():
    message = 'You selected: \n'
    if cb_var1.get() == 1:
        message = message + 'Option 1\n' # this will concatenate option 1 to the original message!!
    if cb_var2.get() == 1:
        message = message + 'Option 2\n'
    if cb_var3.get() == 1:
        message = message + 'Option 3\n'

    messagebox.showinfo("selection", message)

leftframe = Frame(root)
leftframe.pack(side='left')

rightframe = Frame(root)
rightframe.pack(side='right')

cb_var1 = IntVar()
cb_var2 = IntVar()
cb_var3 = IntVar()

# set int var objects to 0, which means not selected

cb_var1.set(0)
cb_var2.set(0)
cb_var3.set(0)

# note they are already set to 0 by default even if you do not use the set method

checkbox1 = Checkbutton(leftframe, text='Option 1', variable=cb_var1)
checkbox1.pack()

checkbox2 = Checkbutton(leftframe, text='Option 2', variable=cb_var2)
checkbox2.pack()

checkbox3 = Checkbutton(leftframe, text='Option 3', variable=cb_var3)
checkbox3.pack()

okbutton = Button(rightframe, text='Okay', command=show_choice)
okbutton.pack(side='left')

quitbutton = Button(rightframe, text='Quit', command=root.destroy)
quitbutton.pack(side='right')

root.mainloop()