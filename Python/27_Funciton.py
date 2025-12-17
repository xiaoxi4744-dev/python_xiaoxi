 #Function คือ บล็อกของโค้ดที่สามารถนำกลับมาใช้ใหม่ได้ โดยสามารถรับค่าเข้า (parameters) และส่งค่ากลับ (return value) ได้
 
def Hello(time,Username,age): # ฟังก์ชัน Hello ที่รับพารามิเตอร์ชื่อ Username
     print("Hello World!", time , Username)
     print("Age : ", age)
     

# ข้อมูลแบบลำดับ *data [XX]
# ข้อมูลแบบกำหนดชื่อ **data "XX"
def save(**data):
    print(f"ชื่อพนักงาน {data["name"]}, แผนก {data["department"]} ")
    print(f"เงินเดือน {data["salary"]} บาท")
    print(f"ที่อยู่ {data["address"]} ")
    print("=========")

def Add(num1):
    print(f"==========แม่ {num1}===========")
    for i in range(1, 12+1):
        print(f"{num1} x {i} = {num1*i}")
     
mytime = "Evening"
Hello(mytime,"xiao",19) #arguments  # เรียกใช้ฟังก์ชัน Hello
Hello(mytime,"Ling",20)
Add(5)    # เรียกใช้ฟังก์ชัน Add

# เรียกใช้ฟังก์ชัน save parameters 3 ค่า
save(name="Xiao",department="IT",salary=70000,address="Bangkok")
save(name="Zhifan",department="กราฟฟิก",salary=30000,address="Home")
save(name="Ling",department="sotf",salary=60000,address="Chiangmai")