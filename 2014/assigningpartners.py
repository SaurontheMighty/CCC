n=int(input())
if(n%2==0):
    pairs=[]
    
    a=(input().split(" "))
    b=(input().split(" "))
    for i in range(n):
        if([a[i],b[i]] not in pairs and [b[i],a[i]] not in pairs):
            pairs.append([a[i],b[i]])

    if(len(pairs)!=n/2):
        print("bad")
    else:
        print("good")
else:
    print("bad")