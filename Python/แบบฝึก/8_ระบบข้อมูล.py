
while True:
    
    user = input("Enter Your User: ")
    password = input("Enter Your Password: ")


    if user == "xiaoxi" and password == "1234":
        print("Welcome to python")
        
        while True:
            print("1.ข้อรายชื่อนักเรียน")
            print("2. GPA System")
            print("3.ออกจากระบบ")

            service = int(input("โปรดเลือกระบบที่ต้องการ: "))

            match service:
        
                case 1:
                        
                        Studen = {
                        "zhifan":"100",
                        "lingling":"100",
                        "xiao":"100"
                        }
                        while True:
                            print("ยินดีต้อนรับเข้าสู้ระบบรายชื่อ")
                            
                            print("========================")
                            fix = input("แก้ข้อโปรดเลือก [Yes 1]/[No 0] : ")
                            if fix == "1" :
                                print("คุณได้เขาสู่ระบบแก้ไขข้อมูล")
                                name = input("ใส่ชื่อนักเรียน : ")
                                score = input("แก้ไขคะแนน")
                                Studen.update({name:score})
                                
                                for key,value in Studen.items():
                                    print("ชื่อ ",key," : คะแนน " ,value)
                            
                                
                            else:
                                print("")
                                break
            
        
                case 2: 
                    print("Welcome GPA system")
                    sub = int(input("จำนวนวิชา: "))  

                    Grades = []
                    Credits = []
                    Subjak = []

                    for i in range(sub):
                        print(f"\n--- วิชา {i+1} ---")
                        subject_name = str(input("กรอกรายชื่อวิชา: "))
                        grade = float(input("กรอกเกรดเฉลี่ย: "))
                        credit = float(input("กรอกหน่วยกิต: "))
                
                        Grades.append(grade)
                        Credits.append(credit)
                        Subjak.append(subject_name)
                
                    total1 = 0
                    total2 = 0

                    for i in range(sub):
                        total1 += Grades[i] * Credits[i]
                        total2 += Credits[i]

                    GPA = total1 / total2

                    print("\n====== ผลลัพธ์ GPA ======")
            
                    for i in range(sub):
                        print("||",Subjak[i],"||",Grades[i],"||",Credits[i],"||")
                
                    print("============================")
                    print("หน่วยกิตรวม: ",total2)
                    print("เกรดเฉลี่ยรวม: ",GPA)
                    print("============================")
                
                case 3:
                    print("ออกจากระบบเรียบร้อยแล้ว")
                    break
            
                case _ :
                    print("กรุณาข้อมูลกรอกใหม่")
                    
    else:
        print("ข้อมูลไม่ถูกต้อง")