l = input()
ii = l.split(" ")
ii = [int(i) for i in ii]
n = ii[0]
k = ii[1]

inp = input()

attractions=inp.split(" ")

attractions = [int(i) for i in attractions]

listofhighs=[]

Z=k
for i in range(0,Z):
    if(n==1):
        break
    set1=[]
    for i in range(0,k):
        set1.append(attractions[i])
    high1 = max(set1)

    set2=[]
    for i in range(k,n):
        set2.append(attractions[i])
    high2 = max(set2)

    listofhighs.append(high1+high2)
    if(k>1 and (n-k+1)<=k):
        k=k-1
    else:
        break
if(n!=1):
    print(max(listofhighs))
else:
    print(attractions[0])
    



