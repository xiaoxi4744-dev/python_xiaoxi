#ระบบแก้ 0
#รายชื่อนักเรียน
j=0

def datastuden(**score):
    print(f"\t|{score["ID"]} .  รายชื่อนักเรียน| {score["name"]}\t|งานที่1 : {score["W1"]}\t|งานที่2 : {score["W2"]}\t|งานที่3 : {score["W3"]}\t|งานที่4 : {score["W4"]}\t|งานที่5 : {score["W5"]}\t|Midterm : {score["Mid"]}\tFinal : {score["Final"]}|")

studants =[
    #1.นายอภิวัฒน์ พิเคราห์งาม
    {"ID":"1","name":"นายอภิวัฒน์ พิเคราห์งาม","W1":100,"W2":0,"W3":0,"W4":0,"W5":0,"Mid":0,"Final":0},
    #2.นายภานุวัชน์ ผองแก้ว
    {"ID":"1","name":"นายภานุวัชน์ ผองแก้ว","W1":100,"W2":0,"W3":0,"W4":0,"W5":0,"Mid":0,"Final":0},
    #3.นายประสิทธิโชค สมใจ
    {"ID":"1","name":"นายประสิทธิโชค สมใจ","W1":100,"W2":0,"W3":0,"W4":0,"W5":0,"Mid":0,"Final":0},
    #4.นางสาวสมศักดิ์ กินแซ่บ
    {"ID":"1","name":"นางสาวสมศักดิ์ กินแซ่บ","W1":100,"W2":0,"W3":0,"W4":0,"W5":0,"Mid":0,"Final":0},
    
    
]

print("ระบบแก้ 0 ในรายวิชาคอมพิวเตอร์")

while True:
        
        print("[ยินดีตอนรรับสู้ระบบแก้ 0 รายวิชาคอมพิวเตอร์]")
        print("1.ตารางสอนของครู : ")
        print("2.คำนวณเกรดในรายวิชานี้ : ")
        print("3.เช็ครายชื่อช่องคะแนน : ")
        print("4.ระบบเช็คพฤติกรรมนักเรียน : ")
        print("5.ออกจากระบบ : ")
        menu = input("เลือกเมนูที่ต้องการ : ")
        match menu:
            case "1":
                print("ยินดีอต้อนรับสู่ระบบ")
                def table(**table):
                    print(f"\t| {table["Day"]}\t|{table["namesubject"]}\t|\t|\t{table["namesubject1"]}\t|")
                    
                    
                def time():
                    print("\t| DAY\t| 08:00-12:00น.\t|\t|\t13:00-16:00น.\t|")
                    
                listname=[
                    {"01":" มีสอนห้อง447 ","02":" ไม่มีคาบสอน "},
                    {"01":" ไม่มีคาบสอน ","02":" ไม่มีคาบสอน "},
                    {"01":" ไม่มีคาบสอน ","02":" ไม่มีคาบสอน "},
                    {"01":" ไม่มีคาบสอน ","02":" ไม่มีคาบสอน "},
                    {"01":" ไม่มีคาบสอน ","02":" ไม่มีคาบสอน "}
                ]
                print("\t+-------------------------------------------------------+")
                time()
                print("\t|-------------------------------------------------------|")
                for i in range(len(listname)):
                    table(Day=i+1,namesubject=listname[i]["01"],namesubject1=listname[i]["02"])
                print("\t+-------------------------------------------------------+")
                    
                pass
            case "2":
                total = []
                j=0
                for i in range(len(studants)):
                    total.append(studants[i]["W1"]+studants[i]["W2"]+studants[i]["W3"]+studants[i]["W4"]+studants[i]["W5"]+studants[i]["Mid"]+studants[i]["Final"])
                print("+---------------------------------------+")
                for i in total:
                    if i >= 80:G="A" 
                    elif i >= 75:G="B+"
                    elif i >= 70:G="B"
                    elif i >= 65:G="D+"
                    elif i >= 60:G="D"
                    elif i >= 55:G="C+"
                    elif i >= 50:G="C"
                    else: G="i"
                    print(f"|\t{studants[0+j]['name']}\t{i} : {G}\t|")
                    j += 1
                print("+---------------------------------------+")
            case "3":
                print("\t+------------------------------------------------------------------------------------------------------------------------------------------------+")
                i = 0
                for data in range(len(studants)):
                    datastuden(ID=(i+1),name=studants[i]["name"],W1=studants[i]["W1"],W2=studants[i]["W2"],W3=studants[i]["W3"],W4=studants[i]["W4"],W5=studants[i]["W5"],Mid=studants[i]["Mid"],Final=studants[i]["Final"])
                    i = i +1
                print("\t+------------------------------------------------------------------------------------------------------------------------------------------------+")
            case "4":
                #ฟังก์ชั่นคะแนน
                
                print("[ยินดีต้อนรับสู่ระบบพฤติกรรม]")
                i = 0
                Studenscore = 100
                #รายชื่อนักเรียน
                for i in range (len(studants)):
                    print(f"\t{i+1}. {studants[i]['name']}\tคะแนนพฤติกรรม\t{Studenscore}")
                #ลบคะแนนนักเรียน
                
            case "5":
                break
            case _:
                print("[ไม่มีรายการนี้]")