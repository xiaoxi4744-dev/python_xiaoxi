custom_data = [ #list of dictionaries
    {"name":"xiao", "type":"member"},
    {"name":"li", "type":"guest"},
    {"name":"wang", "type":"member"},   
]

id = int(input("ป้อนรหัสลูกค้า : "))
print(f"รหัสลูกค้าที่ป้อนคือ {id} : {custom_data[id]['name']}")

match custom_data[id]:
    case {"type" : "member"}:
        print("คุณคือสมาชิกได้รับสิทธิพิเศษ")
    case _:
        print("ไม่ได้เป็นสมาชิก")