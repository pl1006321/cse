# 3 types of widgets; entry, label, and buttons

from tkinter import *

# creating the window
root = Tk()
root.geometry('400x200') # this is for the sizing

# now the title!
root.title('grade average calculator')

# now the label widgets
score1_label = Label(root, text='Enter first score: ')
# every label needs 2 parameters; where its gonna be and the actual text

score1_label.grid(row=0,column=0)
# grid is for where you wanna place it

score2_label = Label(root, text='Enter second score: ')
score2_label.grid(row=1,column=0)

score3_label = Label(root, text='Enter third score: ')
score3_label.grid(row=2,column=0)

# now entry widgets!
score1 = IntVar()
score1_entry = Entry(root, textvariable = score1)
# instead of displaying text, the second parameter is now a variable
score1_entry.grid(row=0,column=1)

score2 = IntVar()
score2_entry = Entry(root, textvariable = score2)
score2_entry.grid(row=1,column=1)

score3 = IntVar()
score3_entry = Entry(root, textvariable=score3)
score3_entry.grid(row=2,column=1)

average_label = Label(root, text='Average: ')
average_label.grid(row=3,column=0)

def get_average(s1, s2, s3):
    sum = float(s1.get()) + float(s2.get()) + float(s3.get())
    average = sum/3
    display_average_label = Label(root, text='%.2f'%average)
    display_average_label.grid(row=3,column=1)

# now for the button widgets!!!
average_button = Button(root, text = 'Average', command = lambda:get_average(score1_entry, score2_entry, score3_entry))
# 3 parameters for button widgets: location, display text, and command
average_button.grid(row=4,column=0)

quit_button = Button(root, text='Quit', command = root.destroy)
quit_button.grid(row=4,column=1)

root.mainloop() # everything that u code has to be before this