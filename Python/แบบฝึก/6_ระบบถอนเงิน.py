atm = int(input("Enter Your Money : "))

n1000 = atm // 1000
atm %= 1000

n500 = atm // 500
atm %= 500

n100 = atm // 100
atm %= 100


if (atm % 2) == 1 :
    print(atm,"ถอนไม่ได้")
else:
    print(f"1000 :  = {n1000} ")
    print(f"500 :  = {n500} ")
    print(f"100 :  = {n100} ")