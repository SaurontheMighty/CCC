n=int(input())
listoflists=[]

def confectionmechanism(cars):
    ideal=sorted(cars)
    a=1
    lake=[]
    branch=[]
    for i in range(len(cars)):
        if(len(branch)<=0):
            if(cars[i]==a):
                lake.append(cars[i])
                a=a+1
            else:
                branch.insert(0,cars[i])
        elif(len(branch)>0):
            if(cars[i]==a):
                lake.append(cars[i])
                a=a+1
            elif(branch[0]==a):
                lake.append(branch[0])
                a=a+1
                branch.pop(0)
            else:
                branch.insert(0,cars[i])
        
    
    if(len(lake)==len(cars)):
        return "Y"
    else:
        lake.extend(branch)
        if(lake==ideal):
            return "Y"
        else:
            return "N"

for i in range(n):
    x=int(input())
    temp=[]
    for j in range(x):
        temp.append(int(input()))
    temp.reverse()
    listoflists.append(temp)

for i in range(n):
    print(confectionmechanism(listoflists[i]))