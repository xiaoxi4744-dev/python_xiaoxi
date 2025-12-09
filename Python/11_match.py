#match 
service = int(input("Enter service number (1-3): "))

match service:
    case 1:
        print("You selected service 1")
    case 2:
        print("You selected service 2")
    case 3:
        print("You selected service 3")
    case _:
        print("Invalid service number")