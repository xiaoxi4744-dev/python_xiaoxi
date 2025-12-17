def table(**Subject):
    print(f"ID : {Subject["ID"]} ชื่อรายวิชา : {Subject["name"]}")
    
idsub = input("[ID] : ")
namesub = input("[NAME] : ")
table(ID=idsub ,name=namesub)