score = int(input("ป้อนคะแนนสอบของนักเรียน : "))

print("----------output-----------")
print("คะแนนสอบของนักเรียนคือ :",score)
grade = None

if score >= 80 and score <= 100:
    grade = "A"
elif score >= 70 and score <= 79:
    grade = "B"
elif score >= 0 and score <= 69:
    grade = "F"
else:
    grade = "คะแนนสอบไม่ถูกต้อง"
    
print("เกรดของนักเรียนคือ", grade)