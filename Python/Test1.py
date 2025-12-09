
user = str(input("Enter Your User: "))
password = int(input("Enter Your Password: "))

if user == "xiaoxi" and password == 1234:
    print("Welcome to python")
else:
    print("Fail")

print("1.Game")
print("2. GPA System")
print("3.")

service = int(input("โปรดเลือกระบบที่ต้องการ: "))

match service:
    
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

        print("\n==== ผลลัพธ์ GPA ====")
        
        for i in range(sub):
            print("||",Subjak[i],"||",Grades[i],"||",Credits[i],"||")
            
        print("============================")
        print("หน่วยกิตรวม: ",total2)
        print("เกรดเฉลี่ยรวม: ",GPA)
        print("============================")
        