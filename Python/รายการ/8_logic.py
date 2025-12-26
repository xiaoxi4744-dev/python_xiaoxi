username = str(input("Enter username: "))
password = int(input("Enter password: "))
print("----------output-----------")
if username == "admin" and password == 1234:
    print("Login successful")
else:
    print("Login failed")