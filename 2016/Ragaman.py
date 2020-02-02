line1 = input()
line2 = input()
anagram1={}
anagram2={}
letters=[]


if("*" in line2):
    for i in range(0,len(line1)):
        char=line1[i]
        if char not in anagram1:
            anagram1.update({char: 1})
            letters.append(char)
        else:
            x=anagram1.get(char)+1
            anagram1.update({char: x})

    for i in range(0,len(line2)):
        char=line2[i]
        if char not in anagram2:
            anagram2.update({char: 1})
        else:
            x=anagram2.get(char)+1
            anagram2.update({char: x})

    for i in range(0,len(anagram1)):
        anagram1["*"]=anagram1[letters[i]]
        anagram1.pop(letters[i])
        if(anagram1==anagram2):
            print("A")
            break
        else:
            anagram1[letters[i]]=anagram1["*"]
            anagram1.pop("*")
    print("N")
else:
    print("N")

