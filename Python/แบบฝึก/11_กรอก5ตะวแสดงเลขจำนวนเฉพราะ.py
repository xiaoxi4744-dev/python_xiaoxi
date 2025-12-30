Array = []
for i in range (0,5,1):
    Num = int(input("Enter Number : "))
    Array.append(Num)
    
for N in Array :
    if N <= 1 : continue
    
    p = True
    
    for S in range (2,N):
        if N % S == 0: 
            p = False
            break
        
    if p:
        print(N)