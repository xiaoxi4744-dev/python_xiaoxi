#ฟังก์ชั่นจัดการ List

sum = ["com,atk,agi,mmo,cov,hok"]

sum.append("[123]") #เริ่มแค่ 1 รายการ

sum.extend(["[ads","uom]"]) #หลายรายการ

sum.insert(0,"attakc") #แทรกระหว่าง Array

sum.remove("attakc") #ลบตัวที่ต้องการ

#sum.clear() #ลบหมด

print(sum)