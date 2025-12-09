total = 0
while True:
    number = int(input("Add number : "))
    if number <= 0:
        break
    total += number
print("Total =", total)
print("Goodbye!")