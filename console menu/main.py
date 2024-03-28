# Import the necessary packages
from consolemenu import *
from consolemenu.items import *

# Create the menu
menu = ConsoleMenu("Attendance", "CSE")

# Create some items

# MenuItem is the base class for all items, it doesn't do anything when selected
# menu_item = MenuItem("Menu Item")

def function1():
    print("hiiiii")
    x = input("hit enter to return to menu: ")
    # forces system to wait for user input before exiting immediately

def function2(name):
    print("hi " + name )
    x = input("hit enter to return to menu: ")

# A FunctionItem runs a Python function when selected
# DO NOT USE OPEN CLOSE PARENTHESES WHEN CALLING FUNCTIONS
function_item_1 = FunctionItem("calling function 1", function1)
function_item_2 = FunctionItem("calling function 2", function2, ("poopy",))
# these parameters will be sent as tuples

# A CommandItem runs a console command # WE ARE NOT USING THIS
# command_item = CommandItem("Run a console command",  "touch hello.txt")

# A SelectionMenu constructs a menu from a list of strings
# selection_menu = SelectionMenu(["item1", "item2", "item3"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
# submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

# Once we're done creating them, we just add the items to the menu
# menu.append_item(menu_item)
menu.append_item(function_item_1)
menu.append_item(function_item_2)
# menu.append_item(command_item)
# menu.append_item(submenu_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()