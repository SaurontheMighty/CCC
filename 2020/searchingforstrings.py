needle = input()
haystack = input()
r=0
nlen= len(needle)
def ch(needle,nlen):
    n={}
    for i in range(nlen):
        if(needle[i] not in n):
            n.update({needle[i]: 1})
        else:
            x=n[needle[i]]
            n.update({needle[i]:x+1})
    return n
n=ch(needle,nlen)
hlen=len(haystack)
b=0
b1=nlen
sublist=[]
while(b1<=hlen):
    sub=haystack[b:b1]
    b=b+1
    b1=b1+1
    if(sub not in sublist):
        sublist.append(sub)
        if(ch(sub,nlen)==n):
            r=r+1

print(r)
