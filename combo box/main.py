from tkinter import *
from tkinter import messagebox
from tkinter import ttk # needed for combo box

root = Tk()
root.geometry("300x200")
root.title("Combo Box")
root.resizable(False, False)

months = ('January','February','March','April','May','June','July','August',"September",'October','November','December')
combobox_label = Label(text='Please select a month: ')
combobox_label.pack(fill='x',padx=5,pady=5)

selectedmonth = StringVar()
month_combobox = ttk.Combobox(root,textvariable=selectedmonth)
month_combobox.pack(fill='x',padx=5,pady=5)

month_combobox['values']=months
month_combobox['state']="readonly"

def show_choice(month):
    msg = f"You selected {month_combobox.get()}!"
    messagebox.showinfo("Selected",msg)

# okbutton = Button(root,text='Ok',command=lambda:show_choice(month_combobox))
# okbutton.pack()

# this is how to bind!
month_combobox.bind("<<ComboboxSelected>>",show_choice)

root.mainloop()

