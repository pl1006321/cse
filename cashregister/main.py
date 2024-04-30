from RetailItem import *
from CashRegister import *

Item1 = RetailItem('Jacket',12,59.95)
Item2 = RetailItem('Designer Jeans',40,34.95)
Item3 = RetailItem('Shirt',20,24.95)

print(f"1. {Item1}")
print(f"2. {Item2}")

cart = CashRegister()

choice = input('Enter the number corresponding to the item you\'d like to purchase, or click enter to stop: ')
while choice:
    if choice == '1':
        cart.purchase_item(Item1)
    if choice == '2':
        cart.purchase_item(Item2)
    if choice == '3':
        cart.purchase_item(Item3)
    choice = input('Enter the number corresponding to the item you\'d like to purchase, or click enter to stop: ')

print('The items in your cart are: ')
cart.show_item()

