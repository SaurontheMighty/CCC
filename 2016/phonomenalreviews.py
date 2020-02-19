nm=input().split(" ")
n=int(nm[0])
m=int(nm[1])
restaurants = input().split(" ")
restaurants=[int(i) for i in restaurants]

allpoints=[]
for i in range(n-1):
    temp=input().split(" ")
    temp=[int(i) for i in temp]
    allpoints.append(temp)

start=restaurants[0]
end = restaurants[1]
depth=0


def explore(original,start,end, depth):
    poi=[]
    depth=depth+1
    for i in range(len(allpoints)):
        if(start in allpoints[i]):
            poi.extend(allpoints[i])
    
    c=[]
    for i in (poi):
        if(i!=start and i!=end and i!=original):
            c.append(i)
        elif(i==end):
            return depth
    
    if(len(c)==0):
        return -1
    else:
        for i in range(len(c)):
            depth1 = explore(start,c[i],end,depth)
            if(depth1!=-1 and depth1!=None):
                return depth1

sumof=0
if(m>2):
    for i in range(0,m-2):
        depth=0
        start=restaurants[i]
        end=restaurants[i+1]
        sumof=sumof+explore(start, start, end, depth)
    print(sumof-1)
else:
    start=restaurants[0]
    end=restaurants[1]
    print(explore(start,start,end,depth))