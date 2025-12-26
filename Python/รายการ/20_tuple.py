#()
sum = ("com",159.9,0)
name,price,stock = sum
# sum[0] = "dkd" ไม่สามารถแก้ไขได้
print(type(sum))
print(len(sum))

print(name)
print(sum[1])
print(sum[2])

for item in sum: #คำสั่งลัด กำหนดตัวแปรอะไรก็ได้จากนั้น ก็หยิบเอาตัวแปรที่เก็บค่าเอาไว้ ถ้ามีเท่าไหร่ใตัวนั้นมันจะดึง มาในลูปวนจนครบ
    print(item)