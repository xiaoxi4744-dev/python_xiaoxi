#Literal Pattern , Wildcard Pattern _ , Capture Patternจะใช้ในกรณีที่เราต้องการจับค่าคงที่ ,
service = 100
match service:
    case 1:print("ฝากเงิน")
    case 2:print("ถอนเงิน")
    case 3:print("ยอดเงินคงเหลือ")
    case service:print(f"ช้อมูลไม่ถูกต้อง หมายเลข {service} ในระบบมีบริการเพียง 3 อย่าง")
    
    
#ตัวอย่างที่2 Guard Filter
score = int(input("กรุณากรอกคะแนนของคุณ : "))
print(f"คะแนนของคุณคือ {score} คะแนน")

match score:
    case 100:
        print("สอบได้เต็ม")
    case score if score>=50 and score<100:
        print("ผ่านการสอบ")
    case _:
        print(f" {score} สอบไม่ผ่าน")
        
#ตัวอย่างที่3 Or Pattern
data = input("ป้อนชื่อนำ้ของคุณ : ")
match data:
    case "เด็กหชาย" | "นาย":
        print("ชาย")
    case "เด็กหญิง" | "นางสาว" | "นาง":
        print("หญิง")
    case _:
        print("ไม่ระบุเพศ")
        
        
#ตัวอย่างที่4 Sequence Pattern
data1 = [] 
#มีข้อมูล 0 ตัว
#data1 = [1,2] #มีข้อมูล 2 ตัว
#data1 = [1,2,3] #มีข้อมูล 3 ตัว
match data1:
    case []:
        print("ไม่มีข้อมูล")
    case [1,2]:
        print("ข้อมูลมี 2 ตัว คือ 1 กับ 2")
    case [1,2,3]:
        print("ข้อมูลมี 3 ตัว คือ 1 กับ 2 กับ 3")
        
#ตัวอย่างที่5 Mapping Pattern
data2 = {"name":"xiao",
         "type":"member"
         }
match data2:
    case {"type":"member"}:
        print("คุณคือสมาชิกได้รับสิทธิพิเศษ")
    case _:
        print("ไม่ได้เป็นสมาชิก")