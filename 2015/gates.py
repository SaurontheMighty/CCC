gates = int(input())
airplanes= int(input())
preferences=[]
assignedgates=[]

for i in range(airplanes):
    preferences.append(int(input()))

preferences.sort()
for i in range(airplanes):
    for j in range(1,preferences[i]):
        if(j not in assignedgates):
            assignedgates.append(j)
    
print(len(assignedgates))