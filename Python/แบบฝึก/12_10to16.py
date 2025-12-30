
num = []
number10 = int(input("Enter number : "))

while number10 > 0 :
    num.append(number10 % 16)
    number10 //= 16
    
num.reverse()

print("เลขฐาน 16 คือ :",end=" ")

for i in num:
    if i == 15 : print("F")
    elif i == 14 : print("E")
    elif i == 13 : print("D")
    elif i == 12 : print("C")
    elif i == 11 : print("B")
    elif i == 10 : print("A")
    else: print(i,end="")