#คำสั่งเงื่อนไข if-else
score = int(input("ป้อนคะแนนสอบของนักเรียน : "))

print("----------output-----------")
print("คะแนนสอบของนักเรียนคือ :",score)
if score < 0:
    print("คะแนนสอบไม่ถูกต้อง")
elif score >= 50:
    print("เกรดของนักเรียนคือ A")
else :
    print("เกรดของนักเรียนคือ F")