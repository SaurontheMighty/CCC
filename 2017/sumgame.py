import sys
n = int(sys.stdin.readline())
swifts = []
semaphores = []


x = sys.stdin.readline()
y=x.rstrip("\n")
swifts=y.split(" ")

    
x = sys.stdin.readline()
y=x.rstrip("\n")
y=y.split(" ")
semaphores=x.split()


sum1=0
sum2=0

flag=0
g=[]

append = g.append
for i in range(0,n):
    sum1+=int(swifts[i])
    sum2+=int(semaphores[i])
    if(sum1==sum2):
        append(i+1)
    else:
        append(0)

sys.stdout.write(str(max(g)))
