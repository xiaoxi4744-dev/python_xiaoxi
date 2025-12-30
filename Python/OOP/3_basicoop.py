#constructor

class Empy:
    
    def __init__(data,ename,salary,department):
        data.name = ename
        data.salary = salary
        data.dpm = department
        
    def bob(data):
        print("ชื่อ {} ".format(data.name))
        print("เงินเดือน {} ".format(data.salary))
        print("ตำแหน่ง {} ".format(data.dpm))
        
    def __hello__(data):
        print("call Destuctor")
        
boby = Empy("xiao",10000,"CEO")
boby.bob()

print("เป็นสามาชิกไหม : ",end=" ")
print(isinstance(boby,Empy))
print(dir(boby))
print(boby.__class__)