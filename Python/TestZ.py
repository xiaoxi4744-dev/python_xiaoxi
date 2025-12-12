#ระบบเก็บคะแนนนักเรียน
Studen = {
    "zhifan":"100",
    "lingling":"100",
    "xiao":"100"
}


name = input("ใส่ชื่อ : ")
score = input("ใส่คะแนน : ")
Studen.update({name:score}) 

for key,value in Studen.items():
    print(key," = ",value)