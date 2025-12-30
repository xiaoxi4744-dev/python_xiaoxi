def OOP():
    return "Wellcome to OOP"
    
def appen(item):
    Sum = []
    i = 0
    for i in range(item):
        sum = input(f"Enter Number : {i+1} : ")
        Sum.append(sum)
    
    #return Sum
    for i in range (item):
        print(Sum[i])
        
        
        
class Employee:
    def detail(data,ename,esalary,department):
        data.name = ename
        data.salary = esalary
        data.dpm = department
        
    def showdata(data):
        print("ชื่อพนักงาน : {} ".format(data.name))
        print("เงินเดือน : {} ".format(data.salary))
        print("ตำแหน่ง : {} ".format(data.dpm))

obj1 = Employee()
obj1.detail("xiao",80000,"CEO")

obj2 = Employee()
obj2.detail("lingling",50000,"IT")

obj3 = Employee()
obj3.detail("xiaoling",30000,"IT")

obj1.showdata()
obj2.showdata()