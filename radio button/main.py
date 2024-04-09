# a radio button is a selection option that allows you to select ONE option and then prompt a message

from tkinter import *
from tkinter import messagebox

# creating the window
root = Tk()
root.geometry("300x200")
root.title("Radio button")

# create frames
rb_frame1 = Frame(root)
rb_frame1.pack(side='left')

rb_frame2 = Frame(root)
rb_frame2.pack(side='right')


# creating the radio buttons
radio_var = IntVar()
radiobutton1 = Radiobutton(rb_frame1, text='Option 1', variable=radio_var, value=1)
radiobutton1.pack()

radiobutton2 = Radiobutton(rb_frame1, text='Option 2', variable=radio_var, value=2)
radiobutton2.pack()

radiobutton3 = Radiobutton(rb_frame1, text='Option 3', variable=radio_var,value=3)
radiobutton3.pack()

# okay button
def show_choice():
    messagebox.showinfo("selection","You selected option " + str(radio_var.get()))

ok_button = Button(rb_frame2, text='Okay', command=show_choice)
ok_button.pack(side='left')

# quit button

quit_button = Button(rb_frame2, text='Quit', command=root.destroy)
quit_button.pack(side='right')

root.mainloop()