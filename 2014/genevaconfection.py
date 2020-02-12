n=int(input())

def confectionmechanism(cars):
    if(len(cars)<=2):
        return "Y"
    elif(cars==sorted(cars)):
        return "Y"
    else:
        a=1
        lake=[]
        branch=[]
        i=0
        while i<len(cars):
            if(cars[i]==a):
                lake.append(a)
                a=a+1
                i=i+1
            elif(len(branch)>0 and branch[0]==a):
                lake.append(a)
                branch.pop(0)
                a=a+1
            else:
                branch.insert(0,cars[i])
                i=i+1
        if(len(lake)==len(cars)):
            return "Y"
        else:
            lake.extend(branch)
            if(lake==sorted(cars)):
                return "Y"
            else:
                return "N"
    
alllist=[]
for i in range(n):
    x=int(input())
    temp=[]
    for j in range(x):
        temp.append(int(input()))
    temp.reverse()
    alllist.append(temp)

for i in range(len(alllist)):
    print(confectionmechanism(alllist[i]))

