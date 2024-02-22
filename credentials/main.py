# password must be at least 8 characters long
# at least one uppercase char
# at least one lowercase char
# and at least one numeric dig
# verify the email contains both an @ and a .

# must contain 3 functions: create username, create password, and save password
# maybe create function for verifying password and email??

def verify_username(entry):
    if "@" in entry and "." in entry:
        return 1
    else: return 0


def create_username():
    email = str(input("Please enter a valid email address: "))
    validity = verify_username(email.strip())
    if validity != 1:
        print("Username is not valid. Please try again. ")
    else: return email


isusersped = 1
while isusersped == 1:
    username = create_username()
    if type(username) != str
