Num = []
for i in range(0,10,1):
    num = int(input("กรอกตัวเลข : "))
    Num.append(num)
    
for n in Num:
    if n %2 == 0:
        print(f" {n} ",end=" ")