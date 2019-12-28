n = int(input())
numbers = []

for i in range(n):
    inp = input().split()
    inp = [int(i) for i in inp]
    numbers.append(inp)

for j in range(n*n):
    g=0
    for i in range(0,n):
        if(min(numbers[i])!=numbers[i][0]):
              numbers=list(zip(*numbers[::-1]))
              break
        else:
            g=g+1
        columns=list(zip(*numbers))

        if(min(columns[i])==numbers[0][i]):
            g=g+1
        else:
            numbers=list(zip(*numbers[::-1]))
            break
    if(g==n*2):
        for i in range(0,n):
            print(*numbers[i], sep=" ")
        break


