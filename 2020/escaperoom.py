rows = int(input())
columns=int(input())

rmatrix=[]

for i in range(rows):
    rmatrix.append(input().split(' '))
    rmatrix[i] = [int(j) for j in rmatrix[i]]

def recursion(point,parents):
    poi=[]

    for i in range(1,point+1):
        if(point%i==0 and i<=rows and point/i<=columns and (rmatrix[i-1][int(point/i)-1] not in parents)):
            if(i==rows and int(point/i)==columns):
                return 'yes'
            else:
                poi.append([i,int(point/i)])
    if (len(poi)==0):
        return 'no'
    else:
        for i in range(len(poi)):
            n=rmatrix[poi[i][0]-1][poi[i][1]-1]
            parents.append(point)
            x=recursion(n,parents)
            if(x=='yes'):
                return 'yes'
        return 'no'

print(recursion(rmatrix[0][0],[]))
