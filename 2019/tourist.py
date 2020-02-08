input1=input().split(" ")
n=int(input1[0])
k=int(input1[1])
attractions=input().split(" ")
z=k

if(n>z):
    maximum=0
    for i in range(z):
        a=attractions[0:k]
        b=attractions[k:n]
        m=int(max(a))+int(max(b))
        if(m>maximum):
            maximum=m

        if(n-k+1<=z and n%z!=0):
            k=k-1
        else:
            break
        if((max(a)<max(b)) or (int(sorted(attractions)[-1])+int(sorted(attractions)[-2]))==maximum):
            break
    print(maximum)
else: 
    print(max(attractions))
