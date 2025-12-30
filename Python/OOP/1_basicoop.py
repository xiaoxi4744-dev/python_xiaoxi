class Empy:
    def data1(data,ename,salary,department):
        data.name = ename
        data.salary = salary
        data.dpm = department
        
    def bob(data):
        print("ชื่อ {} ".format(data.name))
        print("เงินเดือน {} ".format(data.salary))
        print("ตำแหน่ง {} ".format(data.dpm))
        
boby = Empy()
boby.data1("bibi",100000,"CEO")

boby.bob()