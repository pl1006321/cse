from Person import *
from Customer import *
yes_or_no = 'Yes'

name = input("Please enter your name: ")
address = input("Please enter your address: ")
phone_num = input("Please enter a valid phone number: ")
customer_num = input("Please enter your customer number: ")
mailing_list = input("Would you like to be on the mailing list? Enter either yes or no: ")
mailing_list = mailing_list.lower()
mailing_list = mailing_list.strip()
if mailing_list == 'yes':
    mailing_list = True
elif mailing_list == 'no':
    mailing_list = False
    yes_or_no = 'No'

customer = Customer(name,address,phone_num,customer_num,mailing_list)

input("\nData saved! Click enter to continue:")

print('\n======== CUSTOMER INFO ========')
print(f'Name: {customer.get_name()}')
print(f'Address: {customer.get_address()}')
print(f'Phone number: {customer.get_phone_num()}')
print(f'Customer number: {customer.get_customer_num()}')
print(f'Registered for mailing list: {yes_or_no.title()}')