# write a program that keeps usernames (email addresses) and passwords in a dictionary
# as key value pairs. the program should display a menu that lets the user add a new
# username and password, look up a persons password, change an existing password, and
# delete an existing username and password. the program should pickle the dict and save
# it to a file when the user exits the program. each time the program starts, it
# should retrieve the dictionary from the file and unpickle it

# each username must have an @ and a .
# each pw must be at least 8 chars, one uppercase n one lowercase, n one dig

creds = {}


def menu():
    print("Welcome to the menu!")
    print("\nPlease select from the following list of options.")
    print("\n - Add username and password: 1")
    print(" - Look up a password: 2")
    print(" - Change an existing password: 3")
    print(" - Delete an existing username and password: 4")
    entry = int(input("\nPlease enter your selection: "))
    return entry


def verify_email(entry):
    if "@" in entry and "." in entry:
        return 1
    else:
        return 0


def create_user():
    email = str(input("\nPlease enter a valid email address: "))
    validity = verify_email(email.strip())
    while not validity:
        print("\nUsername is not valid. Please try again.")
        email = str(input("\nPlease enter a valid email address: "))
        validity = verify_email(email.strip())
    print("\nUsername successfully saved!")
    return email


def verify_pw(entry):
    if entry.isupper() or entry.islower():
        return False
    elif len(entry) < 8 or entry.isalpha() or entry.isdecimal():
        return False
    else:
        return True


def create_pw():
    print(
        "\nPassword must contain: \n -at least one uppercase letter \n -at least one lowercase letter \n -at least one numeric digit \n -at least 8 total characters")
    pw = str(input("\nPlease enter a valid password: "))
    validity = verify_pw(pw.strip())
    while not validity:
        print("\nPassword is not valid. Please try again. ")
        pw = str(input("\nPlease enter a valid password: "))
        validity = verify_pw(pw)
    return pw


def create_userpw():
    user = create_user()
    password = create_pw()
    creds.update({user: password})
    print(creds)


def pw_lookup():
    print("this is for looking up a pw")


def change_pw():
    print("this is for changing a pw")


def delete_creds():
    print("this is for deleting a user and pw")


choice = menu()
if choice == 1:
    create_userpw()
elif choice == 2:
    pw_lookup()
elif choice == 3:
    change_pw()
else:
    delete_creds()

