#ARITHMETIC SQUARE
#SaurontheMighty
import sys
#Input
i1=sys.stdin.readline()
i2=sys.stdin.readline()
i3=sys.stdin.readline()

l1=[]
l2=[]
l3=[]

l1x=[]
l2x=[]
l3x=[]

xn1=0
xn2=0
xn3=0

yn1=0
yn2=0
yn3=0

i1=i1.rstrip("\n")
i2=i2.rstrip("\n")
i3=i3.rstrip("\n")

l1=i1.split(" ")
l2=i2.split(" ")
l3=i3.split(" ")

for i in  range(0,3):
    if(l1[i]=="X"):
        xn1=xn1+1
        l1x.append(i)
    if(l2[i]=="X"):
        xn2=xn2+1
    if(l3[i]=="X"):
        xn3=xn3+1

        
if(l1[0]=="X"):
    yn1=yn1+1
if(l2[0]=="X"):
    yn1=yn1+1
if(l3[0]=="X"):
    yn1=yn1+1
if(l1[1]=="X"):
    yn2=yn2+1
if(l2[1]=="X"):
    yn2=yn2+1
if(l3[1]=="X"):
    yn2=yn2+1
if(l1[2]=="X"):
    yn3=yn3+1
if(l2[2]=="X"):
    yn3=yn3+1
if(l3[2]=="X"):
    yn3=yn3+1

#Processing
if(xn1==1):
    if(l1[2]=="X"):
        first=int(l1[0])
        second=int(l1[1])

        d=second-first
        l1[2]=str(int(second+d))
        
    if(l1[1]=="X"):
        first=int(l1[0])
        third=int(l1[2])
        d=(third-first)/2
        l1[1]=str(int(first+d))

    if(l1[0]=="X"):
        second=int(l1[1])
        third=int(l1[2])

        d=third-second
        l1[0]=str(int(second-d))

#l2
if(xn2==1):        
    if(l2[2]=="X"):
        first=int(l2[0])
        second=int(l2[1])

        d=second-first
        l2[2]=str(int(second+d))
            
    if(l2[1]=="X"):
        first=int(l2[0])
        third=int(l2[2])

        d=(third-first)/2
        l2[1]=str(int(first+d))

    if(l2[0]=="X"):
        second=int(l2[1])
        third=int(l2[2])

        d=third-second
        l2[0]=str(second-d)

#l3
if(xn3==1):
    if(l3[2]=="X"):
        first=int(l3[0])
        second=int(l3[1])

        d=second-first
        l3[2]=str(int(second+d))
            
    if(l3[1]=="X"):
        first=int(l3[0])
        third=int(l3[2])

        d=(third-first)/2
        l3[1]=str(int(first+d))

    if(l3[0]=="X"):
        second=int(l3[1])
        third=int(l3[2])

        d=third-second
        l3[0]=str(int(second-d))

xn1=0
xn2=0
xn3=0

yn1=0
yn2=0
yn3=0

for i in  range(0,3):
    if(l1[i]=="X"):
        xn1=xn1+1
        l1x.append(i)
    if(l2[i]=="X"):
        xn2=xn2+1
    if(l3[i]=="X"):
        xn3=xn3+1

        
if(l1[0]=="X"):
    yn1=yn1+1
if(l2[0]=="X"):
    yn1=yn1+1
if(l3[0]=="X"):
    yn1=yn1+1
if(l1[1]=="X"):
    yn2=yn2+1
if(l2[1]=="X"):
    yn2=yn2+1
if(l3[1]=="X"):
    yn2=yn2+1
if(l1[2]=="X"):
    yn3=yn3+1
if(l2[2]=="X"):
    yn3=yn3+1
if(l3[2]=="X"):
    yn3=yn3+1

#Processing2
if(yn1==1):
    if(l3[0]=="X"):
        first=int(l1[0])
        second=int(l2[0])

        d=second-first
        l3[0]=str(int(second+d))
            
    if(l2[0]=="X"):
        first=int(l1[0])
        third=int(l3[0])

        d=(third-first)/2
        l2[0]=str(int(first+d))

    if(l1[0]=="X"):
        second=int(l2[0])
        third=int(l3[0])

        d=third-second
        l1[0]=str(int(second-d))

#l2
if(yn2==1):
    if(l3[1]=="X"):
        first=int(l1[1])
        second=int(l2[1])

        d=second-first
        l3[1]=str(int(second+d))
            
    if(l2[1]=="X"):
        first=int(l1[1])
        third=int(l3[1])

        d=(third-first)/2
        l2[1]=str(int(first+d))

    if(l1[1]=="X"):
        second=int(l2[1])
        third=int(l3[1])

        d=third-second
        l1[1]=str(int(second-d))


#l3
if(yn3==1):
    if(l3[2]=="X"):
        first=int(l1[2])
        second=int(l2[2])

        d=second-first
        l3[2]=str(int(second+d))
            
    if(l2[2]=="X"):
        first=int(l1[2])
        third=int(l3[2])

        d=(third-first)/2
        l2[2]=str(int(first+d))

    if(l1[2]=="X"):
        second=int(l2[2])
        third=int(l3[2])

        d=third-second
        l1[2]=str(int(second-d))


print(l1[0]+" "+l1[1]+" "+l1[2])
print(l2[0]+" "+l2[1]+" "+l2[2])
print(l3[0]+" "+l3[1]+" "+l3[2])
