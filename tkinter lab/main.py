# ask for a students:
# school id
# first and last name
# what grade they are in
# current comp sci teacher
# what comp sci courses they've already taken
# after selection, info should be displayed in a message box then saved to a file

# form should include:
# label, entry, radio button, check button, button, and combo box

# ============================================================

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.geometry("600x400")
root.title("Computer Science Student Information Entry")
# root.resizable(False, False)

leftframe = Frame(root)
leftframe.pack(side='left')

rightframe = Frame(root)
rightframe.pack(side='right')

bottomframe = Frame(root)
bottomframe.pack(side='bottom')

id_entry_label = Label(leftframe,text='School ID: ')
id_entry_label.pack(fill='both',padx=20,pady=20)

name_entry_label = Label(leftframe,text='First & last name: ')
name_entry_label.pack(fill='both',padx=20,pady=20)

grade_entry_label = Label(leftframe,text='Current grade: ')
grade_entry_label.pack(fill='both',padx=20,pady=20)

current_teachers_label = Label(leftframe, text='Current Comp Sci Teacher(s): ')
current_teachers_label.pack(fill='both',padx=20,pady=20)

id_number = StringVar()
id_entry = Entry(rightframe,textvariable=id_number)
id_entry.pack(fill='both',padx=20,pady=20)

full_name = StringVar()
full_name_entry = Entry(rightframe,textvariable=full_name)
full_name_entry.pack(fill='x',padx=20,pady=20)

grades = ['9th','10th','11th','12th']
selected_grade = StringVar()
grade_combobox = ttk.Combobox(rightframe,textvariable=selected_grade)
grade_combobox.pack(fill='both',padx=20,pady=20)

grade_combobox['values']=grades
grade_combobox['state']='readonly'

current_courses_label = Label(rightframe,text='Current Comp Sci Course(s): ')
current_courses_label.pack(fill='both',padx=20,pady=20)

cse = IntVar()
cse.set(0)
cse_checkbox = Checkbutton(leftframe,text='Computer Science Essentials (Honors)',variable=cse)
cse_checkbox.pack(fill='both',padx=20,pady=5)

pwp = IntVar()
pwp.set(0)
pwp_checkbox = Checkbutton(leftframe,text='Programming with a Purpose (Honors)',variable=pwp)
pwp_checkbox.pack(fill='both',padx=20,pady=5)

apcsa = IntVar()
apcsa.set(0)
apcsa_checkbox = Checkbutton(leftframe,text='AP Computer Science A',variable=apcsa)
apcsa_checkbox.pack(fill='both',padx=20,pady=5)

apcsp = IntVar()
apcsp.set(0)
apcsp_checkbox = Checkbutton(leftframe,text='AP Computer Science Principles',variable=apcsp)
apcsp_checkbox.pack(fill='both',padx=20,pady=5)

cybersec = IntVar()
cybersec.set(0)
cybersec_checkbox = Checkbutton(leftframe,text='Cyber Security and Defense (Honors)',variable=cybersec)
cybersec_checkbox.pack(fill='both',padx=20,pady=5)

dataarch = IntVar()
dataarch.set(0)



root.mainloop()