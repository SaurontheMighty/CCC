nm = input().split(" ")
n=int(nm[0])
m=int(nm[1])
index = 0
line = 0
listempty = []

grid=[]
for i in range(0,n):
    temp = input()
    c = temp.count("S")
    grid.append(temp)
    if(c!=0):
        index = temp.index("S")
        line = i

c=grid[line].count(".")
if():
    


for i in range(0,n):
    print(*grid[i])
