water1=0
time1=0

water = 350
time = 9

for i in (0,8,1):
    water1+=water
    time1+=time
    
    water *= 1.25
    time *= 1.15
    
print(water1)
print(time1)