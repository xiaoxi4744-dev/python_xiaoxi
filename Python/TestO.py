
start = int(input("Enter start month (1-12): "))
end = int(input("Enter end month (1-12): "))

for number in range (start,end+1):
    print("============Calendar============")
    print("Month : ", number)
    for i in range(1,13):
        print(number,"x",i,"=",number*i)