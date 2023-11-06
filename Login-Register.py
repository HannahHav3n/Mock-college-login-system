import os
import base64
from datetime import datetime


try:
    os.makedirs("Database")
except:
    pass


print(f"Time: {datetime.now().strftime('%H:%M')}")
print("Welcome to the mock college login screen\n")

def check_password(password):
    if len(password) < 15:
        Fail = "True"
    else:
        Fail = "False"
    return Fail



option = input("Login or register [l/r]: ")
if option.lower() == "l":
    username_authenticated = "False"
    password_authenticated = "False"
    authed = "False"
    print("[>] Login system [<]")
    username = input("Username: ")
    password = input("Password: ")
    with open(f"Database/{username}.txt", 'r') as f:
        file_content = f.read()
        file_content_unb64 = base64.b64decode(file_content)
        file_content_unutf = file_content_unb64.decode('utf-8')
        lines = file_content_unutf.splitlines()
        for line in lines:
            if line == f"Username: {username}":
                username_authenticated = "True"
            
            elif line == f"Password: {password}":
                password_authenticated = "True"
    if username_authenticated and password_authenticated == "True":
        print("Logged in")
    else:
        print("Failed to login")



elif option.lower() == "r":
    print("[>] Registration process [<]")
    forename = input("Forename: ")
    surname = input("Surname: ")
    data_of_brith = input("Date of birth: ")
    email = input("Email: ")
    username = input("Username: ")
    while username == forename:
        print("Please choose a username different to your forename")
        username = input("Username: ")
    password = input("Password: ")
    check = check_password(password)
    while check == "True":
        print("Password under 15 charectors please choose a stronger password")
        password = input("Password: ")
        check = check_password(password)     
    data = f"Forename: {forename}\nSurname: {surname}\nD.O.B: {data_of_brith}\nEmail: {email}\nUsername: {username}\nPassword: {password}"
    bytes_data = data.encode('utf-8')
    b64_data = base64.b64encode(bytes_data)
    with open(f"Database/{username}.txt", 'wb') as f:
        f.write(b64_data)
    print("\nSuccesfully registered for mock college thank you for you time you can now login\n")
