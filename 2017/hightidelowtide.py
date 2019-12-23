import sys
n = int(sys.stdin.readline())
heights = ((sys.stdin.readline()).rstrip("\n")).split(" ")
new=[]

low=[]
high=[]
ap1=high.append
ap2=low.append

heights = [ int(x) for x in heights ]

heights.sort()

for i in range(0,n):
    if(n%2==0):
        if(i<int(n/2)):
            ap2(heights[i])
        else:
            ap1(heights[i])
    if(n%2!=0):
        if(i<=int(n/2)):
            ap2(heights[i])
        else:
            ap1(heights[i])

low.sort(reverse=True)
high.sort()

n1=0
n2=0
for i in range(0,n):
    if((i+1)%2==0):
        x=high[n1]
        new.append(x)
        n1+=1
    else:
        x=low[n2]
        new.append(x)
        n2+=1
        
for i in range(0,n):
    sys.stdout.write(str(new[i]))
    sys.stdout.write(" ")
