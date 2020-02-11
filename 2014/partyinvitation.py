k = int(input())
m=int(input())
rounds=[]
for i in range(m):
    rounds.append(int(input()))

friends=[]
for i in range(k):
    friends.append(i+1)

for i in range(len(rounds)):
    for j in range(len(friends)):
        if((j+1)%rounds[i]==0):
            friends[j]="r"
    for j in range(len(friends)):
        if(friends[j]=="r"):
            friends.pop(j)
            if(friends.count("r")==0):
                break

for i in range(len(friends)):
    print(friends[i])