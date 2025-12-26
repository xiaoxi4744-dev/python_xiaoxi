
def tese(**Tese):
    print(f"ชื่อ{Tese["Name"]}\tอายุ{Tese["age"]}\tรายได้{Tese["salary"]}")

data = [
    {"name":"xiao","age":"20","salary":"25000"}
]
tese(Name=data[0]["name"],age=data[0]["age"],salary=data[0]["salary"])