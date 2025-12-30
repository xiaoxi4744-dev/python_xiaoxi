
def datastudens1(**data):
    print(f"ID {data["ID"]} {data["name"]} {data["behavior"]} {data["score"]}")

studens1 = [
    {"01":"นายอภิวัฒน์ พิเคราห์งาม","02":"behavior","03":100},
    {"01":"นายอัตนุย พรมดีมั้ง","02":"behavior","03":100},
    {"01":"นายไบรอั้น เรโนว","02":"behavior","03":100},
    {"01":"นายสมจัย ปราณวารี","02":"behavior","03":100},
]

for i in range (len(studens1)):
    datastudens1(ID=(i+1),name=studens1[i]["01"],behavior=studens1[i]["02"],score=studens1[i]["03"])