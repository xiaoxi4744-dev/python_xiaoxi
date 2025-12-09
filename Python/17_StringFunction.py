
#นี้คือฟังก์ชันสตริงพื้นฐานใน Python 

name = "Xiaoxi"
print(name.upper()) #แปลงเป็นตัวพิมพ์ใหญ่
print(name.lower()) #แปลงเป็นตัวพิมพ์เล็ก
print(name.startswith("Xiao")) #เช็คว่าข้อความขึ้นต้นด้วยอะไร
print(len(name)) #มีจำนวนกี่ตัว

print("ชื่อ {0} อายุ {1} ปี".format("xiao",20)) #ตำแหน่ง


#Ex
name = str(input("Add your name: "))

if name.startswith("Xiao"):
    print("สวัสดีคุณเสี่ยวซี")
elif name.startswith("Li"):
    print("สวัสดีคุณหลี่")
else:
    print("สวัสดีคุณผู้มาใหม่")

#หา string ที่ลงท้ายด้วยคำที่กำหนด
Age = str(input("Enter year of birth: "))
if Age.endswith("20"):
    print("คุณเกิดในปี 2020")
else:
    print("คุณไม่ได้เกิดในปี 2020")

text = "Hello World"
print(text.find("H")) #หาตำแหน่งตัวอักษร

print(text.count("o")) #หาว่ามีกี่ตัว
