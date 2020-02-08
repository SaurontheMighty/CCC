#INPUT
q=int(input())
n=int(input())

dmoj=input().split(" ")
peg=input().split(" ")

#CALC
dmoj=[int(i) for i in dmoj]
dmoj.sort()
peg=[int(i) for i in peg]
peg.sort()

pairs=[]
if(q==2):
    for i in range(n):
        temp=[dmoj[n-1-i],peg[i]]
        pairs.append(temp)
    
    score=0
    for i in range(n):
        score=score+int(max(pairs[i]))
    print(score)
    
elif(q==1):
    for i in range(n):
        temp=[dmoj[n-1-i],peg[n-1-i]]
        pairs.append(temp)
    
    score=0
    for i in range(n):
        score=score+int(max(pairs[i]))
    print(score)