# nuion() , intersectn() , difference() ,set
a = {"Cat", "Dog", "Lion"}
b = {"Lion", "Tiger"}

a.add("หมา")
b.update(("หมู","ฉลาม"))
print(a)
print(b)

print("<=========Data=========>")

animals=b.difference(a)
print(animals)