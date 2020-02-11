n=int(input())
freq=[]
val=[]

for i in range(n):
    x=int(input())
    if(x not in val):
        val.append(x)
        freq.append(1)
    else:
        freq[val.index(x)]=freq[val.index(x)]+1

for i in range(len(freq)):
    for j in range(i+1,len(freq)):
        if(freq[i]>freq[j]):
            temp=freq[j]
            freq[j]=freq[i]
            freq[i]=temp
            temp=val[j]
            val[j]=val[i]
            val[i]=temp

if(freq.count(freq[-1])==1 and freq.count(freq[-2])==1):
    print(abs(val[-1]-val[-2]))
elif(freq.count(freq[-1])==1 and freq.count(freq[-2])>1):
    maxo=0
    maxmax=abs(max(val)-min(val))
    for i in range(len(freq)-1):
        if(freq[i]==freq[-2]):
            max1=abs(val[-1]-val[i])
            if(max1>maxo):
                maxo=max1
            if(maxo==maxmax):
                break
    print(maxo)
elif(freq.count(freq[-1])>1 and freq.count(freq[-2])==1):
    maxo=0
    maxmax=abs(max(val)-min(val))
    for i in range(len(freq)):
        if(freq[i]==freq[-1]):
            max1=abs(val[-2]-val[i])
            if(max1>maxo):
                maxo=max1
            if(maxo==maxmax):
                break
    print(maxo)
elif(freq[-1]==freq[-2]):
    v=[]
    for i in range(len(freq)):
        if(freq[i]==freq[-1]):
            v.append(val[i])
    print(abs(max(v)-min(v)))
else:
    m1=[]
    m2=[]
    maxmax=abs(max(val)-min(val))
    for i in range(len(freq)):
        if(freq[i]==freq[-1]):
            m1.append(val[i])
        if(freq[i]==freq[-2]):
            m2.append(val[i])
    maxo=0
    for i in m1:
        for j in m2:
            max1= abs(i-j)
            if(max1>maxo):
                maxo=max1
            if(maxo==maxmax):
                break
    print(maxo)