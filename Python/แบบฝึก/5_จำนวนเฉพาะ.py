x = int(input("Enter Number : "))
p = 1

if x <=1 :
    p = 0
    
for i in range (2,x-1): # เริ่มที่ 2 วนจนถึง n-1 
    if x % i == 0 :
        p = 0
        break
    
if(p):
    print("Yes")
else:
    print("No")