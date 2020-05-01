n = int(input())
matrix=[]
for i in range(0,n):
    matrix.append(input().split(' '))
    matrix[i]=[int(j) for j in matrix[i]]

matrix.sort()

speeds=[]

for i in range(0,n-1):
    t1=matrix[i][0]
    t2=matrix[i+1][0]
    d1=matrix[i][1]
    d2=matrix[i+1][1]
    speeds.append(abs((d2-d1)/(t2-t1)))


print(max(speeds))