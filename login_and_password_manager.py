users = {}

def add_user():
    user = input("Enter your user name: ")
    if user in users:
        print("Username already exists!")
    else:
        password = input("Enter your password: ")
        users[user] = password
        print(f"user for {user} is successfully added")

def login():
    username = input("Enter your Username: ")
    password = input("Enter your Password: ")
    if username in users and users[username] == password:
        print("Login Successful.")
    else:
        print("Invalid Username or Password")

# function to change the variable to a specific key
def change_password():
    user = input("Enter your user name: ")
    password = input("Enter your password: ")
    if users[user] != password:
        print("Incorrect password")
    elif user not in password:
        print("Username do not exist")
    elif new_password == password:
        print("The New password cannot be the same as the original password")
    else:
        new_password = input("Enter your new password: ")
        users[user] = new_password
        print(f"password for the {user} has been successfully changed")

while True:
    print("1. Register")
    print("2. Change Password")
    print("3. Login")
    print("4. Quit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        change_password()
    elif choice == "3":
        login()
    elif choice == "4":
        break
    else:
        print("Invalid Choice")
