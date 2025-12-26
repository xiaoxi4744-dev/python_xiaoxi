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

#function return
def Get(): # ฟังก์ชัน Get ที่ไม่มีพารามิเตอร์
    return "Beijing" # ส่งค่ากลับเป็นสตริง "Beijing"

mydata = Get() # เก็บค่าที่ได้จากการเรียกใช้ฟังก์ชัน Get ลงในตัวแปร mydata
print("mydata : ", mydata) # แสดงผลลัพธ์ที่ได้จากการเรียกใช้ฟังก์ชัน Get

def getpi():
    return 3.14

rafdius = 5
area = getpi()*rafdius**2
print(f"พื้นที่วงกลม : {area} " )

#Para + reture function
def number(number):
    if number%2 == 0:
        return "Yes"
    else:
        return "No"

def sum(*args):
    total=0
    for item in args:
        total+=item
    return total
print(sum(10,20,30))

#lambda funtion

s=lambda num,n : num**n
print(s(2,4))