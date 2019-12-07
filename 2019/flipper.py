#Flipper
#SaurontheMighty
r1c1=1
r1c2=2
r2c1=3
r2c2=4

translation=input()
length=len(translation)

for i in range(0,length):
    char = translation[i]
    if(char=="H"):
        temp=r1c1
        r1c1=r2c1
        r2c1=temp
        temp=r1c2
        r1c2=r2c2
        r2c2=temp
    if(char=="V"):
        temp=r1c1
        r1c1=r1c2
        r1c2=temp
        temp=r2c1
        r2c1=r2c2
        r2c2=temp

print(r1c1," ",r1c2)
print(r2c1," ",r2c2)
