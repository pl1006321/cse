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
import pickle

template = {'Name': 'N/A','Grade':'N/A','Current Teacher':'N/A','Past / Current Courses': 'N/A'}
compiled = {}

root = Tk()
root.geometry("600x400")
root.title("Computer Science Student Information Entry")
# root.resizable(False, False)

teachers_frame = Frame(root)
teachers_frame.grid(row=4,column=1,rowspan=8,columnspan=2,sticky='NSWE')

buttons_frame = Frame(root)
buttons_frame.grid(row=11,column=1, columnspan=4)

id_entry_label = Label(root,text='School ID: ')
id_entry_label.grid(row=1,column=1,padx=10,pady=5,sticky='W')

name_entry_label = Label(root,text='First & last name: ')
name_entry_label.grid(row=2,column=1,padx=10,pady=5,sticky='W')

grade_entry_label = Label(root,text='Current grade: ')
grade_entry_label.grid(row=3,column=1,padx=10,pady=5,sticky='W')

current_teachers_label = Label(teachers_frame, text='Current Teacher: ')
current_teachers_label.grid(padx=10,pady=10)

id_number = StringVar()
id_entry = Entry(root,textvariable=id_number)
id_entry.grid(row=1,column=2,padx=10,pady=5,sticky='W')

full_name = StringVar()
full_name_entry = Entry(root,textvariable=full_name)
full_name_entry.grid(row=2,column=2,padx=10,pady=5,sticky='W')

grades = ['9th','10th','11th','12th']
selected_grade = StringVar()
grade_combobox = ttk.Combobox(root,textvariable=selected_grade)
grade_combobox.grid(row=3,column=2,padx=10,pady=5,sticky='W')

grade_combobox['values']=grades
grade_combobox['state']='readonly'

current_courses_label = Label(root,text='Past / Current Course(s): ')
current_courses_label.grid(row=1,column=4,padx=10,pady=5,sticky='wens')

cse = IntVar()
cse.set(0)
cse_checkbox = Checkbutton(root,text='Computer Science Essentials (Honors)',variable=cse)
cse_checkbox.grid(row=2,column=4,padx=10,pady=5,sticky='W')

pwp = IntVar()
pwp.set(0)
pwp_checkbox = Checkbutton(root,text='Programming with a Purpose (Honors)',variable=pwp)
pwp_checkbox.grid(row=3,column=4,padx=10,pady=5,sticky='W')

apcsa = IntVar()
apcsa.set(0)
apcsa_checkbox = Checkbutton(root,text='AP Computer Science A',variable=apcsa)
apcsa_checkbox.grid(row=4,column=4,padx=10,pady=5,sticky='W')

apcsp = IntVar()
apcsp.set(0)
apcsp_checkbox = Checkbutton(root,text='AP Computer Science Principles',variable=apcsp)
apcsp_checkbox.grid(row=5,column=4,padx=10,pady=5,sticky='W')

cybersec = IntVar()
cybersec.set(0)
cybersec_checkbox = Checkbutton(root,text='Cyber Security and Defense (Honors)',variable=cybersec)
cybersec_checkbox.grid(row=6,column=4,padx=10,pady=5,sticky='W')

dataarch = IntVar()
dataarch.set(0)
dataarch_checkbox = Checkbutton(root,text='Data Architecture Honors',variable=dataarch)
dataarch_checkbox.grid(row=7,column=4,padx=10,pady=5,sticky='W')

machineai = IntVar()
machineai.set(0)
machineai_checkbox = Checkbutton(root,text='Machine Learning & AI Honors',variable=machineai)
machineai_checkbox.grid(row=8,column=4,padx=10,pady=5,sticky='W')

appinno = IntVar()
appinno.set(0)
appinno_checkbox = Checkbutton(root,text='Application Innovation Honors',variable=appinno)
appinno_checkbox.grid(row=9,column=4,padx=10,pady=5,sticky='W')

internship = IntVar()
internship.set(0)
internship_checkbox = Checkbutton(root,text='Computer Science Internship Honors',variable=internship)
internship_checkbox.grid(row=10,column=4,padx=10,pady=5,sticky='W')

# mr rivero, mr stern, mr baker, mrs demosthenes, mrs behar 

current_teacher = StringVar()
current_teacher.set(0)

rivero_button = Radiobutton(teachers_frame,text='Mr. Rivero',variable=current_teacher,value='Mr. Rivero')
rivero_button.grid(padx=20,pady=5,sticky='W')

stern_button = Radiobutton(teachers_frame,text='Mr. Stern',variable=current_teacher,value='Mr. Stern')
stern_button.grid(padx=20,pady=5,sticky='W')

baker_button = Radiobutton(teachers_frame,text='Mr. Baker',variable=current_teacher,value='Mr. Baker')
baker_button.grid(padx=20,pady=5,sticky='W')

demosthenes_button = Radiobutton(teachers_frame,text='Mrs. Demosthenes',variable=current_teacher,value='Mrs. Demosthenes')
demosthenes_button.grid(padx=20,pady=5,sticky='W')

behar_button = Radiobutton(teachers_frame,text='Mrs. Behar',variable=current_teacher,value='Mrs. Behar')
behar_button.grid(padx=20,pady=5,sticky='W')

# buttons!

def picklefile():
    f=open("info.pkl",'wb')
    pickle.dump(compiled,f)
    f.close()

def loadfile():
    f=open('info.pkl','rb')
    compiled=pickle.load(f)
    f.close()

def class_selection():
    selected_classes= []
    if cse.get() > 0: 
        selected_classes.append("Computer Science Essentials Honors")
    if pwp.get() > 0:
        selected_classes.append("Programming with a Purpose Honors")
    if apcsa.get() > 0:
        selected_classes.append("AP Computer Science A")
    if apcsp.get() > 0:
        selected_classes.append("AP Computer Science Principles")
    if cybersec.get() > 0:
        selected_classes.append("Cyber Security & Defense Honors")
    if dataarch.get() > 0:
        selected_classes.append("Data Architecture Honors")
    if machineai.get() > 0:
        selected_classes.append("Machine Learning & AI Honors")
    if appinno.get() > 0:
        selected_classes.append("Application Innovation Honors")
    if internship.get() > 0:
        selected_classes.append("Computer Science Internship Honors")
    return selected_classes

def error_msg():
    messagebox.showinfo("Error","One or more fields has been left empty. Please enter all required fields and try again.")

def save_info():
    global compiled
    if not id_number.get() or not selected_grade.get() or not full_name.get() or not current_teacher.get() or not class_selection():
        error_msg()
        return
    compiled[id_number.get()] = template.copy() 
    compiled[id_number.get()]['Name'] = full_name.get()
    compiled[id_number.get()]['Grade'] = selected_grade.get()
    compiled[id_number.get()]['Current Teacher'] = current_teacher.get()
    compiled[id_number.get()]['Past / Current Courses'] = class_selection()
    picklefile()


def show_info(idnumber):
    temp = compiled[idnumber]
    message = 'ID number: ' + str(idnumber) + '\n' + 'Full name: ' + temp['Name'] + '\n' + 'Current Grade: ' + temp['Grade'] + '\n' + 'Current Teacher: ' + temp['Current Teacher']
    message = message + '\n' + 'Past / Current Courses: ' 
    for x in temp['Past / Current Courses']:
        if len(temp['Past / Current Courses']) == 1:
            message = message + x
        else:
            message = message + x + ', '
    messagebox.showinfo('Registered Info', message)

def okay_function():
    save_info()
    show_info(id_number.get())
    picklefile()

def lookup(idnumber):
    try:
        loadfile()
    except:
        pass
    show_info(idnumber)


ok_button = Button(buttons_frame,text='Save',command=okay_function)
ok_button.grid(row=1,column=1,padx=5,pady=5)

quit_button = Button(buttons_frame,text='Quit',command=root.destroy)
quit_button.grid(row=1,column=2,padx=5,pady=5)

id_lookup_label = Label(buttons_frame,text='Enter ID to look up saved info: ')
id_lookup_label.grid(row=1,column=3,padx=5,pady=5)

schoolid = StringVar()
id_entry = Entry(buttons_frame,textvariable=schoolid)
id_entry.grid(row=1,column=4,padx=5,pady=5,sticky='e')

lookup_button = Button(buttons_frame,text='ID Lookup',command=lambda:lookup(str(schoolid.get())))
lookup_button.grid(row=1,column=5,padx=5,pady=5,sticky='e')

root.mainloop()
