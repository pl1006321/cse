# password must be at least 8 characters long
# at least one uppercase char
# at least one lowercase char
# and at least one numeric dig
# verify the email contains both an @ and a .

# must contain 3 functions: create username, create password, and save password
# maybe create function for verifying password and email??

list = []

def verify_username(entry):
    if "@" in entry and "." in entry:
        return 1
    else: return 0

def create_username():
    email = str(input("Please enter a valid email address: "))
    validity = verify_username(email.strip())
    if not validity:
        while validity == 0:
          print("\nUsername is not valid. Please try again. ")
          email = str(input("\nPlease enter a valid email address: "))
          validity = verify_username(email.strip())

def verify_password(entry):
  if entry.isupper() or entry.islower():
    return False
  if len(entry) < 8 or entry.isalpha() or entry.isdecimal():
    return False
  else: return True

def password_exists(pw):
  with open("passwords.txt", "r") as f:
      for line in f:
          if "Password: " + pw + "\n" in line:
              return False
          else: return True

def create_password():
  print("Password must contain: \n -at least one uppercase letter \n -at least one lowercase letter \n -at least one numeric digit \n -at least 8 total characters")
  password = str(input("\nPlease enter a valid password: "))
  validity = verify_password(password) and password_exists(password)
  if not validity:
    while validity == 0:
      if not verify_password(password):
        print("\nPassword is not valid. Please try again. ")
        password = str(input("\nPlease enter a valid password: "))
        validity = verify_password(password) and password_exists(password)
      if not password_exists(password):
        print("\nPassword already exists.")
        password = str(input("\nPlease enter a new valid password: "))
        validity = verify_password(password) and password_exists(password)
  return password

create_username()
validpassword = create_password()
print("\nPassword has been saved.\n")

def save_password(pw):
  f=open("passwords.txt", "a")
  f.write(str(pw))
  f.write("\n")
  f.close()

save_password(validpassword)

# how do i use a try except block???