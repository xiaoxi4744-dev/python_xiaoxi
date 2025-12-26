i = 0
sum = 0
quests = []
#กรอกค่าของนักเรียน
def studenplus():
    global i
    global sum 
    i = int(input("กรุณากรอกลำกับนักเรียน : "))
    sum = int(input("กรุฌาระบุคะแนน : "))
    studens1[i]["03"] += sum
    
#เพิ่มเควสให้นักเรียน
def Quest():
    global quests
    quests = []
    quest = input("ระบบสิ่งที่จะให้ทำ : ")
    sc = input("กรอกคะแนนเมื่อเสร็จ : ")
    quests.append({
        "Quests": quest,
        "Score": sc
    })
    
    print(quests[0]["Quests"])
    print(f" {quests[0]["Score"]} คะแนน")

def datastudens1(**data1): 
    print(f"ID {data1["ID"]} {data1["name"]} {data1["behavior"]} {data1["score"]}")
    
studens1 = [
    {"01":"นายอภิวัฒน์ พิเคราห์งาม","02":"behavior","03":100},
    {"01":"นายอัตนุย พรมดีมั้ง","02":"behavior","03":100},
    {"01":"นายไบรอั้น เรโนว","02":"behavior","03":100},
    {"01":"นายสมจัย ปราณวารี","02":"behavior","03":100},
]

print("เข้าสู้ระบบแอดมิน")
while True:
    useser = input("กรุณากรอกบัญชี : ")
    password = input("กรุณากรอกรหัสผ่าน : ")
    
    if useser == "admin" and password == "1234":
    
        while True:
                print("ยินดีต้อนรับเข้าสู้ระบบ")
                for i in range(len(studens1)):
                            datastudens1(ID=(i+1),name=studens1[i]["01"],behavior=studens1[i]["02"],score=studens1[i]["03"])
                            pass
                service = input("เลือกรายการ : ")
            #เมนู
                match service:
                    case "1":
                        Quest()
                        
                    case "2":
                        studenplus()
                    case _:
                        pass
                        
                for i in range(len(studens1)):
                            datastudens1(ID=(i+1),name=studens1[i]["01"],behavior=studens1[i]["02"],score=studens1[i]["03"])