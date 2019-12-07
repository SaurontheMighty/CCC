#Pretty Average Primes
#SaurontheMighty
import sys, math
no=int(sys.stdin.readline())
nlist=[]
ablist=[]

def primeCheck(x):
    for i in range(2,int(x**(0.5))+1):
        if(x%i==0):
            return False
    return True

def f(n):
    for x in range(2,n+1):
        y=(2*n)-x
        if(primeCheck(x) and primeCheck(y)):
            return x, y

for i in range(0,int(no)):
    n=int(sys.stdin.readline())
    nlist.append(n)
    a, b=f(n)
    ablist.append(str(a)+" "+str(b))

for i in range(0,no):
    print(ablist[i])
