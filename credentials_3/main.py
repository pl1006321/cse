import pickle

creds = {}


# creds will be empty upon every run of the code
# u have to use loadfile to acc load in the dictionary data 
# also DEFINE CREDS AS GLOBAL in every func or itll be silly 

def picklefile():
    global creds
    f = open("credentials.pkl", "wb")
    pickle.dump(creds, f)
    f.close()


def loadfile():
    global creds
    f = open("credentials.pkl", "rb")
    creds = pickle.load(f)
    f.close()


try:
    loadfile()
except:
    pass


def emailalreadyexists():
    print(
        "\nEmail is already registered with a password. Please register a new email, or change the password under the existing email.")
    entry = input("\nClick enter to return to the menu: ")
    print("\n")


def emaildoesntexist():
    print(
        "\nEmail is not registered with a password. Please enter an existing email, or register a new email and password.")
    entry = input("\nClick enter to return to the menu: ")
    print("\n")


def menu():
    print("====================================================\n")
    print("Welcome to the menu!")
    print("\nPlease select from the following list of options.")
    print("\n - Add username and password: 1")
    print(" - Look up a password: 2")
    print(" - Change an existing password: 3")
    print(" - Delete an existing username and password: 4")
    print(" - Exit the program: 5")
    try:
        entry = int(input("\nPlease enter your selection: "))
        return entry
    except:
        return 0


def runmenu():
    exit = 0
    while exit == 0:
        entry = menu()
        if entry == 1:
            if create_userpw() == 0:
                emailalreadyexists()
        elif entry == 2:
            if pw_lookup() == 0:
                emaildoesntexist()
        elif entry == 3:
            if change_pw() == 0:
                emaildoesntexist()
        elif entry == 4:
            if delete_creds() == 0:
                emaildoesntexist()
        elif entry == 5:
            exit = 1
        elif entry == 0:
            print("\nEntry was not valid. \n\nPlease enter an option from the menu.")
            yippee = input("\nClick enter to return to the menu: ")
            print("\n")


def verify_email(entry):
    if "@" in entry and "." in entry:
        return 1
    else:
        return 0


def create_user():
    global creds
    email = str(input("\nPlease enter a valid email address: "))
    validity = verify_email(email.strip())
    while not validity:
        print("\nUsername is not valid. Please try again.")
        email = str(input("\nPlease enter a valid email address: "))
        validity = verify_email(email.strip())
    if email in creds.keys():
        return 0
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
    global creds
    user = create_user()
    if user == 0:
        return 0
    password = create_pw()
    creds[user] = password
    picklefile()
    print("\nUsername and password have been saved!\n")
    entry = input("Click enter to return to the menu: ")
    print("\n")


def pw_lookup():
    global creds
    email = str(input("\nEnter an existing email: "))
    if email not in creds.keys():
        return 0
    password = creds[email]
    print("\nThe password registered is: \n")
    print(password)
    entry = input("\nClick enter to return to the menu: ")
    print("\n")


def change_pw():
    global creds
    email = str(input("\nEnter an existing email: "))
    if email not in creds.keys():
        return 0
    password = create_pw()
    creds.update({email: password})
    picklefile()
    print("\nPassword has been updated!")
    entry = input("\nClick enter to return to the menu: ")
    print("\n")


def delete_creds():
    global creds
    email = str(input("\nEnter an existing email: "))
    if email not in creds.keys():
        return 0
    password = creds[email]
    print("\nThe password registered is: \n")
    print(password)
    try:
        entry = int(input("\nAre you sure you'd like to delete? \n\nEnter 1 for yes, 2 for no: "))
        if entry == 1:
            creds.pop(email)
            picklefile()
            print("\nRegistered email and password have been deleted.")
        entry = input("\nClick enter to return to the menu: ")
        print("\n")
    except:
        print("\nEntry was not valid. Please start over.")
        yippee = input("\nClick enter to return to the menu: ")
        print("\n")


runmenu()