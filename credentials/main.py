# password must be at least 8 characters long
# at least one uppercase char
# at least one lowercase char
# and at least one numeric dig
# verify the email contains both an @ and a .

# must contain 3 functions: create username, create password, and save password
# maybe create function for verifying password and email??

import os

def verify_username(entry):
    if "@" in entry and "." in entry:
        return 1
    else: return 0


def create_username():
    email = str(input("Please enter a valid email address: "))
    validity = verify_username(email.strip())
    if not validity:
        while validity == 0:
          print("Username is not valid. Please try again. ")
          email = str(input("Please enter a valid email address: "))
          validity = verify_username(email.strip())
    else: return email

def verify_password(entry):
  if entry.isupper() or entry.islower():
    return False
  if len(entry) < 8 or entry.isalpha() or entry.isdecimal():
    return False
  else: return True


def create_password():
  print("Password must contain: \n -at least one uppercase letter \n -at least one lowercase letter \n -at least one numeric digit \n -at least 8 total characters")
  password = str(input("Please enter a valid password: "))
  validity = verify_password(password)
  if not validity:
    while validity == 0:
      print("Password is not valid. Please try again. ")
      password = str(input("Please enter a valid password: "))
      validity = verify_password(password)
  else: return password

validusername = create_username()
print("Username has been saved.")
validpassword = create_password()
print("Password has been saved.")

f=open("passwords.txt", "a")
f.write("\n Username: " + str(validusername))
f.write("\n Password: " + str(validpassword))
f.close()
