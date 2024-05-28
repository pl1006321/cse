from consolemenu import *
from consolemenu.items import *
from Cart import *
from Object import *
import pickle

final_file = {'inventory': {}, 'cart': {}}
inventory = final_file['inventory']
cart = final_file['cart']

def pickle_file():
  global final_file, inventory, cart
  f=open("data.pkl", "wb")
  pickle.dump(final_file,f)
  f.close()

def load_file():
  global final_file, inventory, cart
  f=open("data.pkl","rb")
  final_file = pickle.load(f)
  f.close()
  inventory = final_file['inventory']
  cart = final_file['cart']

def create_item():
  global final_file, inventory
  try:
   name = str(input('\nEnter the name of the item you\'d like to add: '))
  except:
    return 0
  try:
    price = float(input('Enter the price of the item: '))
  except:
    return 0
  try:
    inv = int(input('Enter the inventory amount of the item: '))
  except:
    return 0
  if inv <= 0:
    return 0
  item = Object(name, price, inv, 0)
  inventory[name] = item
  pickle_file()
  print('=====================================================')
  print("               Item added successfully!               ")
  print('=====================================================')
  print('\n')
  return 1

def display_inventory():
  print('=====================================================')
  print('=================  ITEM INVENTORY  ==================')
  print('=====================================================')
  count = 1
  for x in inventory:
    item = inventory[x]
    print(f'\nItem {count}:\n')
    item.display()
    count += 1

def display_cart():
  print('=====================================================')
  print('===================  CART ITEMS  ====================')
  print('=====================================================')
  count = 1
  for x in cart:
    item = cart[x]
    print(f'\nItem {count}:\n')
    item.display()
    count += 1

def manually_edit_inventory():
  display_inventory()
  try:
    choice = int(input('\nEnter the number of the item you\'d like to edit: '))
  except:
    return 0
  temp = []
  for x in inventory.values():
    temp.append(x)
  try:
    item = temp[choice-1]
  except:
    return 0
  print(f'\nItem being edited: {item.get_name()}')
  try:
    new_amt = int(input('\nEnter the adjusted inventory amount for the item: '))
  except:
    return 0
  if new_amt <= 0:
    return 0
  item.set_inv(new_amt)
  pickle_file()
  print("\n             Item edited successfully!             ")
  print("\n              Loading new inventory...              \n")
  display_inventory()
  return 1

def revenue_report(): # CHECK AFTER YOU MAKE CHECKOUT FUNCTION
  global final_file, inventory, cart
  total_rev = 0.00
  for x in inventory.keys():
    item = inventory[x]
    amt_sold = item.get_amt_sold()
    rev = amt_sold * item.get_price()
    total_rev = total_rev + rev
    print(f'{item.get_name()}: {amt_sold} sold || total: ${rev:.2f}')
  print(f'Total Revenue: ${total_rev:.2f}')

def add_item_to_cart():
  global final_file, inventory, cart
  inventory = final_file['inventory']
  cart = final_file['cart']
  display_inventory()
  try:
    choice = int(input('\nEnter the number of the item you\'d like to add to cart: '))
  except:
    return 0
  temp = []
  for x in inventory.values():
    temp.append(x)
  try:
    item = temp[choice-1]
  except:
    return 0
  print(f'\nItem being added to cart: {item.get_name()}')
  try:
    amount = int(input('\nEnter the amount you\'d like to add to cart: '))
  except:
    return 0
  if amount > item.get_inv():
    print('\nAmount inputted exceeds the amount in inventory.')
    return 0
  elif amount <= 0:
    return 0
  if item.get_name() in cart.keys():
    temp_item = cart[item.get_name()]
    old_amt = int(temp_item.get_amt())
    temp_item.set_amt(old_amt + amount)
    new_item = temp_item
  else:
    new_item = Cart_Item(str(item.get_name()), float(item.get_price()), int(item.get_inv()), int(item.get_amt_sold()), amount)
    cart[item.get_name()] = new_item
  print(f'\nQuantity {amount} of {item.get_name()} has been added to cart.')
  pickle_file()
  new_item.display()

def remove_item_from_cart():
  global final_file, inventory, cart
  display_cart()
  try:
    choice = int(input('\nEnter the number of the item you\'d like to remove from your cart: '))
  except:
    return 0
  temp = []
  for x in cart.values():
    temp.append(x)
  try:
    item = temp[choice-1]
  except:
    return 0
  print(f'\nItem being removed from cart: {item.get_name()}')
  print(f'\nAre you sure you\'d like to remove this from your cart?')
  try:
    choice2 = int(input('Enter 1 for yes, 2 for no: '))
  except:
    return 0
  if choice2 == 2:
    print('Item has not been removed.')
    return 1
  elif choice == 1:
    del cart[item.get_name()]
    print('\nItem has been removed from cart.')
    pickle_file()
    return 1
  else:
    return 0

def customer_receipt():
  global final_file, inventory, cart
  total = 0.00
  for x in cart:
    item = cart[x]
    amt = item.get_amt()
    price = item.get_price()
    item_rev = (amt * price)
    item_rev = round(item_rev, 2)
    total = total + item_rev
    print(f'\n{item.get_name()} : {amt} bought || ${item_rev}')
  print(f'\nTotal before taxes: ${total:.2f}')
  taxes = (total*0.07)
  total = total + taxes
  print(f'Applied taxes: ${taxes:.2f}')
  print(f'Total price: ${total:.2f}')

def checkout():
  global final_file, inventory, cart
  display_cart()
  print(f'\nAre you sure you\'d like to checkout with your current cart?')
  try:
    choice2 = int(input('Enter 1 for yes, 2 for no: '))
  except:
    return 0
  if choice2 == 2:
    print('Cart has not been checked out.')
    return 1
  if choice2 != 1:
    return 0
  for x in cart.keys():
    cart_item = cart[x]
    inv_item = inventory[x]
    amt_in_cart = cart_item.get_amt()
    inv_item.set_amt_sold(inv_item.get_amt_sold() + amt_in_cart)
    inv_item.set_inv(inv_item.get_inv() - amt_in_cart)
  customer_receipt()
  cart.clear()
  pickle_file()

def error_msg():
  print('Input was invalid. Please try again.')

# MENU

def add_item_menu():
  if create_item() == 0:
    error_msg()
  a = input('Click enter to continue. ')

def manually_change_inv_menu():
  if manually_edit_inventory() == 0:
    error_msg()
  a = input('\nClick enter to continue. ')

def show_inv_menu():
  display_inventory()
  a = input('\nClick enter to continue. ')

def print_rev_report_menu():
  revenue_report()
  a = input('\nClick enter to continue. ')

def show_cart_menu():
  display_cart()
  a = input('\nClick enter to continue. ')

def add_item_to_cart_menu():
  if add_item_to_cart() == 0:
    error_msg()
  a = input('\nClick enter to continue. ')

def remove_item_from_cart_menu():
  if remove_item_from_cart() == 0:
    error_msg()
  a = input('\nClick enter to continue. ')

def checkout_cart_menu():
  if checkout() == 0:
    error_msg()
  a = input('\nClick enter to continue. ')

menu = ConsoleMenu('Virtual Storefront')

add_item_selection = FunctionItem('Owner - Add item(s)',add_item_menu)
manually_changing_inv_selection = FunctionItem('Owner - Manually Change Inventory',manually_change_inv_menu)
show_inventory_selection = FunctionItem('Owner - Show Inventory', show_inv_menu)
print_rev_report_selection = FunctionItem('Owner - Print Revenue Report',print_rev_report_menu)
show_cart_selection = FunctionItem('Customer - Show Cart', show_cart_menu)
add_item_to_cart_selection = FunctionItem('Customer - Add Item to Cart',add_item_to_cart_menu)
remove_item_from_cart_selection = FunctionItem('Customer - Remove Item from Cart',remove_item_from_cart_menu)
checkout_cart_selection = FunctionItem('Customer - Checkout Cart',checkout_cart_menu)

menu.append_item(add_item_selection)
menu.append_item(manually_changing_inv_selection)
menu.append_item(show_inventory_selection)
menu.append_item(print_rev_report_selection)
menu.append_item(show_cart_selection)
menu.append_item(add_item_to_cart_selection)
menu.append_item(remove_item_from_cart_selection)
menu.append_item(checkout_cart_selection)

try:
  load_file()
except:
  pass
menu.show()