#Voronoi Villages
#SaurontheMighty

n = int(input())#number of villages
vp = []#voronoi positions

for i in range(0,n):
    pos = float(input())
    vp.append(pos)

vp.sort()

size=[]
for i in range(1,n-1):
    size_v = -(vp[i-1]+vp[i])/2 +(vp[i]+vp[i+1])/2
    size.append(size_v)

size.sort()
print(size[0])
