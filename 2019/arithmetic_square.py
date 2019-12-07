#ARITHMETIC SQUARE
#SaurontheMighty
import sys
i1=sys.stdin.readline()
i2=sys.stdin.readline()
i3=sys.stdin.readline()

l1=[]
l2=[]
l3=[]

i1=i1.rstrip("\n")
i2=i2.rstrip("\n")
i3=i3.rstrip("\n")

l1=i1.split(" ")
l2=i2.split(" ")
l3=i3.split(" ")

spos1=[]
spos2=[]
spos3=[]

d=0

for i in range(0,3):
    if(l1[i]!="X"):
        spos1.append(i)
    if(l2[i]!="X"):
        spos2.append(i)
    if(l3[i]!="X"):
        spos3.append(i)    


print(l1[0]," ",l1[1]," ",l1[2])
print(l2[0]," ",l2[1]," ",l2[2])
print(l3[0]," ",l3[1]," ",l3[2])

