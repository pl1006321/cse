import pickle

total_atd = {}
attendance_template = {"M": "P", "T": "P", "W": "P", "TH": "P", "F": "P"}
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']


def pickle_file():
    global total_atd
    f = open("attendance.pkl", "wb")
    pickle.dump(total_atd, f)
    f.close()


def load_file():
    global total_atd
    f = open("attendance.pkl", "rb")
    total_atd = pickle.load(f)
    f.close()


def add_student():
    name = input("Enter the first and last name of a student: ")
    total_atd[name] = attendance_template.copy()
    pickle_file()
    return


def atd_letter_sorter(x):
    if x == 'P':
        status = "Present"
    elif x == 'T':
        status = 'Tardy'
    else:  # x == 'A'
        status = 'Absent'
    return status


def day_letter_sorter(x):
    if x == 1:
        day = 'M'
        name = 'Monday'
    elif x == 2:
        day = 'T'
        name = 'Tuesday'
    elif x == 3:
        day = 'W'
        name = 'Wednesday'
    elif x == 4:
        day = 'TH'
        name = 'Thursday'
    elif x == 5:
        day = 'F'
        name = 'Friday'
    else:
        return 0
    return day


def student_atd_print(x):
    print("\n=========================")
    print("\nMonday: " + x[0])
    print("Tuesday: " + x[1])
    print("Wednesday: " + x[2])
    print("Thursday: " + x[3])
    print("Friday: " + x[4])


def attendance_by_student():
    name = input("Enter the first and last name of an existing student: ")
    if name not in total_atd.keys():
        input(
            "Student does not exist. Please retry and enter an existing student, or add a new student. \nClick enter to continue: ")
        return 0
    temp_attendance = []
    for x in total_atd[name]:
        temp = total_atd[name]
        atd_letter = temp[x]
        status = atd_letter_sorter(atd_letter)
        temp_attendance.append(status)
    return temp_attendance


def day_selection_menu():
    try:
        number = int(input(
            "Please select what day of attendance you'd like to view: \n\n -For Monday, enter 1\n -For Tuesday, enter 2\n -For Wednesday, enter 3\n -For Thursday, enter 4\n -For Friday, enter 5\n\n"))
    except:
        return 0
    day = day_letter_sorter(number)
    if not day:
        return 0
    return day


def attendance_by_day(day):
    print("\n=========================\n")
    for student in total_atd.keys():
        atd_dict = total_atd[student]
        status = atd_dict[day]
        print(student + ": " + status)


def taking_attendance():
    try:
        number = int(input(
            "Please select what day you'd like to take attendance for: \n\n -For Monday, enter 1\n -For Tuesday, enter 2\n -For Wednesday, enter 3\n -For Thursday, enter 4\n -For Friday, enter 5\n\n"))
    except:
        return 0
    day = day_letter_sorter(number)
    if not day:
        return 0
    print("\n=========================\n")
    print("Enter P for present, T for tardy, and A for absent.")
    print("\n=========================\n")
    for student in total_atd.keys():
        student_atd = total_atd[student]
        status = input(student + ": ")
        if status != 'P' and status != 'A' and status != 'T':
            return 0
        student_atd[day] = status
        pickle_file()


def editing_attendance():
    name = input("Enter the first and last name of an existing student: ")
    if name not in total_atd.keys():
        input(
            "Student does not exist. Please retry and enter an existing student, or add a new student. \nClick enter to continue: ")
        return 0
    try:
        number = int(input(
            "Please select what day you'd like to edit attendance for: \n\n -For Monday, enter 1\n -For Tuesday, enter 2\n -For Wednesday, enter 3\n -For Thursday, enter 4\n -For Friday, enter 5\n\n"))
    except:
        return 0
    day = day_letter_sorter(number)
    if not day:
        return 0
    print("\n=========================\n")
    print("Enter P for present, T for tardy, and A for absent.")
    print("\n=========================\n")
    # not complete yet!


# MENU

from consolemenu import *
from consolemenu.items import *


def add_student_menu():
    add_student()
    input("\n=========================\n\nSaved! \n\n=========================\n\nClick enter to continue: ")


def view_atd_byday_menu():
    day = day_selection_menu()
    if not day:
        print("Entry was invalid. Please try again.")
        input("Click enter to continue: ")
        return
    attendance_by_day(day)
    input("\n=========================\n\nClick enter to continue: ")


def view_atd_bystd_menu():
    temp = attendance_by_student()
    if not temp:
        return
    student_atd_print(temp)
    input("\n=========================\n\nClick enter to continue: ")


def take_attendance_menu():
    if taking_attendance() == 0:
        print("Entry was invalid. Please try again. ")
        input("Click enter to continue: ")
        return
    print("\n=========================\n")
    input("Click enter to continue: ")


def editing_atd_menu():
    print("editing attendance")
    x = input("\nclick enter to continue")


menu = ConsoleMenu("Classroom Attendance")

adding_student_selection = FunctionItem("Add new student", add_student_menu)
viewing_attendance_byday_selection = FunctionItem("View attendance by day", view_atd_byday_menu)
viewing_attendance_bystudent_selection = FunctionItem("View attendance by student", view_atd_bystd_menu)
taking_attendance_selection = FunctionItem("Take Attendance for the day", take_attendance_menu)
editing_attendance_selection = FunctionItem("Edit student attendance", editing_atd_menu)

menu.append_item(adding_student_selection)
menu.append_item(viewing_attendance_byday_selection)
menu.append_item(viewing_attendance_bystudent_selection)
menu.append_item(taking_attendance_selection)
menu.append_item(editing_attendance_selection)

try:
    load_file()
except:
    pass
menu.show()
print(str(total_atd))