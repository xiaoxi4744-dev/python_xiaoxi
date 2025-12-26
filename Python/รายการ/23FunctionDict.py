# keys() values() get(key) items() clear() pop(key) update({key,value})
Color = {
    "Red":"แดง",
    "Green":"เขียว",
    "Blue":"น้ำเงิน",
    "Yellow":"เหลือง"
}
main = Color.copy() #ก๊อปก่อนแก้ไข หรือ เพิ่ม

# Color.pop("Blue") #ลบตามที่อยาก

# Color.clear() #ลบทั้งหมด

Color.update({"Box":"สี่เหลี่ยม"}) #เพิ่มข้อมูล

Color.update({"Red":"แดงอ่อน"}) #แก้ไข

print(Color.keys()) #เอาตัวข้างหน้า

print(Color.values()) #เอาตัวข้างหลัง

print(Color.items()) #เอามาทั้งหมด

print("=====================") 
for key,value in Color.items(): #วนทั้งหมด
    print(key , "=", value)
    
print("=====================") 
print(Color.get("Red"))

print(main)