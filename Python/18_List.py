#เก็บข้อมูลหลายตัว 
sub = [0,1,2,3,4,5,6,7,8,9]

for i in range(0,3,1):
    product = str(input("Add : "))
    sub[i] = product
    print(sub[i])

print("========================")
for i in range(0,3,1):
    print(sub[i])