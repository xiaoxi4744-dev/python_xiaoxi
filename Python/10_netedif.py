#netedif
username = str(input("Enter username: "))
password = int(input("Enter password: "))
print("----------output-----------")
if username == "member" and password == 1234:
    print("Login successful")
    print("ฝากเงิน")
    print("ถอนเงิน")
    service = int(input("Enter service (1/2): "))
    if service == 1:
        print("ฝากเงิน")
    elif service == 2:
        print("ถอนเงิน")
    else:
        print("ไม่มีบริการนี้")
else:
    print("Login failed")
