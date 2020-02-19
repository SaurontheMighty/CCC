numberofpieces=int(input())
pieces=input().split(" ")
pieces = [int(i) for i in pieces]

if((sum(pieces)-max(pieces))>max(pieces)):
    pieces.sort()
    sumof=pieces[0]+pieces[-1]
    n=pieces.count(sumof)
    print(str(int((numberofpieces-n)/2)+n)+" "+str(int(numberofpieces%2)+1))

    
else:
    print("1 "+str(int(numberofpieces*(numberofpieces-1)/2)))
