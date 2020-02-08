num = int(input())
nA = int(input())
sizeList=[]

for i in range(num):
    sizeList.append(input())

requests=[]
for i in range(nA):
    requests.append(input().split(" "))

n=0
for i in range(nA):
    number=int(requests[i][1])
    if(number<=num):
        size=requests[i][0]
        if((size in sizeList[number-1]) or (size=="M" and sizeList[number-1]=="L") or (size=="S" and sizeList[number-1]=="L") or (size=="S" and sizeList[number-1]=="M")):
            sizeList[number-1]="r"
            n=n+1
    
print(n)