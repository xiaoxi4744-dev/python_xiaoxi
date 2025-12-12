num = int(input("Add number : "))
N = [] #list คือค่าที่เก็บไว้

while num > 0:
    N.append(num % 2)   #   เอาเศษที่ได้ไปเก็บไว้ใน Array || list
    num //= 2           #   หาค่าแล้วลดค่าไป 2

N.reverse()

print("Binary =", end=" ") #end= คือไม่เริ่มบรรทัดใหม่

for i in N: # วนเอาค่าใน N มา
    print(i, end="")