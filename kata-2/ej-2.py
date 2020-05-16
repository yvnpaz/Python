"""
...
"""
password = "password"
password_user = input("Introduce the password: ")

if password == password_user.lower():
    print("Password correct.")
else:
    print("Password incorrect.")