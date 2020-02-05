l1 = input().split(" ")
l2 = input().split(" ")
l3 = input().split(" ")

matrix=[]
matrix.append(l1)
matrix.append(l2)
matrix.append(l3)

def row():
    for i in range(0,3):
        t1 = matrix[i][0]
        t2 = matrix[i][1]
        t3 = matrix[i][2]

        c= matrix[i]
        n = c.count("X")
        if(n==1):
            if(t1=="X"):
                t1= int(2*int(t2)-int(t3))
            elif(t2=="X"):
                t2= int(int(t1)+(int(t3)-int(t1))/2)
            elif(t3=="X"):
                t3= int(2*int(t2)-int(t1))

        temp=[]
        temp.append(t1)
        temp.append(t2)
        temp.append(t3)
        matrix.pop(i)
        matrix.insert(i,temp)

def column():
    for i in range(0,3):
        c1=matrix[0][i]
        c2=matrix[1][i]
        c3=matrix[2][i]

        temp = [c1,c2,c3]
        n = temp.count("X")
        if(n==1):
            if(c1=="X"):
                c1= int(int(c2)-(int(c3)-int(c2)))
            elif(c2=="X"):
                c2= int(int(c1)+(int(c3)-int(c1))/2)
            elif(c3=="X"):
                c3= int(int(c2)+(int(c2)-int(c1)))

        matrix[0][i]=c1
        matrix[1][i]=c2
        matrix[2][i]=c3

row()
column()

c1=matrix[0].count("X")
c2=matrix[1].count("X")
c3=matrix[2].count("X")

if(c1==2 and c2==2 and c3==2):
    r=0
    for i in range(0,3):
        m = matrix[1][i]
        if(m!="X"):
            r=m
    matrix[1] = [r,r,r]
    row()
    column()
    row()

c1=matrix[0].count("X")
c3=matrix[2].count("X")

m=zip(matrix[0],matrix[1],matrix[2])

r1=m[0].count("X")
r3=m[2].count("X")

if((c1==0 or c3==0) and (r1==0 or r3==0)):
    if()

for i in range(0,3):
    for j in range(0,3):
        print(matrix[i][j],end=" ")
    print()
