# password must be at least 8 characters long
# at least one uppercase char
# at least one lowercase char
# and at least one numeric dig
# verify the email contains both an @ and a .

# must contain 3 functions: create username, create password, and save password
# maybe create function for verifying password and email??

existingpws = []

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

def filetolist():
  try:
    f=open("passwords.txt", 'r')
    for x in f:
      existingpws.append(x.strip("\n"))
    f.close()
  except:
    print("Something went wrong!")


filetolist()

def password_exists(pw):
  if pw in existingpws:
    return 0
  else: return 1

def create_password():
  print("Password must contain: \n -at least one uppercase letter \n -at least one lowercase letter \n -at least one numeric digit \n -at least 8 total characters")
  password = str(input("\nPlease enter a valid password: "))
  validity = verify_password(password) and password_exists(password)
  while not validity:
    while not verify_password(password):
      print("\nPassword is not valid. Please try again. ")
      password = str(input("\nPlease enter a valid password: "))
      verify_password(password)
    while not password_exists(password):
      print("\nPassword already exists. Please enter a new password. ")
      password = str(input("\nPlease enter a valid password: "))
      password_exists(password)
    validity = password_exists(password) and verify_password(password)
  return password

create_username()
print("\nSuccess! Now, create a password. \n")
validpassword = create_password()
print("\nPassword has been saved.\n")

def save_password(pw):
    f=open("passwords.txt", "a")
    f.write(str(pw) + "\n")
    f.close()

save_password(validpassword)
