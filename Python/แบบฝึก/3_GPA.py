G = []
C = []
S = []

for i in range (0,2+1,1):
    print(f"\n======= Round {i+1} ======")
    Subject = str(input("Enter Name Subject : "))
    Grade = float(input("Enter Your Grede Point Average : "))
    Credit = float(input("Enter Your Credits : "))
#list
    S.append(Subject)   #Array รวมของ ชื่อวิชา
    G.append(Grade)     #Array รวมของ เกรดของวิชา
    C.append(Credit)    #Array รวมของ หน่วยกิต
    
    t1 = 0  
    t2 = 0  
#สูตรหาเกรดเฉลี่ย
for i in range (0,2+1,1):
    t1 += G[i]*C[i] #ผลรวมเกรด
    t2 += C[i]      #หน่วยกิตรวมสูตร
    
GPA = t1 /t2

print("\n=========[Result]========")
print(S)    #ชื่อวิชาทั้งหมด
print(t2)   #หน่วยกิตรวม
print(GPA)  #เกรดเฉลี่ยรวม