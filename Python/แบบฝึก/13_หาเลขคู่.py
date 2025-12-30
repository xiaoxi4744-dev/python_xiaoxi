Num = []

for i in range (0,10,1):
    Num.append(int(input("enternumber ")))
    
for item in Num:
    if item % 2 == 0 : print(item,end=" ")