line1 = input()
line2 = input()
letters=[]
etters=[]

for i in range(0, len(line1)):
    if(line1[i] not in letters):
        letters.append(line1[i])

for i in range(0, len(line2)):
    if(line2[i] not in etters and line2[i]!="*"):
        etters.append(line2[i])

counter=True
    
for i in letters:
    if(line1.count(i)<line2.count(i)):
        counter=False
        print("N")
        break

if(counter==True):
    if(all(x in letters for x in etters)): 
        print("A")
    else:
        print("N")
