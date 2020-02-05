n = int(input())
numbers=[]
for i in range(0,n):
    j=int(input())
    if(j!=0):
        numbers.append(j)
    else:
        numbers.pop()

sume=0
for i in range(len(numbers)):
    if(numbers[i]!=-1):
        sume = sume+numbers[i]

print(sume)