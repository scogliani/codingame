letters = ""
res = input()
for tmp in res:
    letter = ""
    letter += bin(ord(tmp))[2:]
    
    if len(bin(ord(tmp))[2:]) < 7:
        letter = "0" + letter
        
    letters += letter

ith = 0
l = []
for e in letters:
    
    if l != []:
        if e == "1" and l[ith][0] == "00":
            l.append(["0", 1])
            ith += 1
        elif e == "0" and l[ith][0] == "0":
            l.append(["00", 1])
            ith += 1
        else:
            l[ith][1] += 1
    
    else:
        if e == "1":
            l.append(["0", 1])
        else:
            l.append(["00", 1])

for i in range(len(l)-1):
    print(l[i][0] + " " + l[i][1]*"0", end=" ")

print (l[len(l)-1][0]+" "+l[len(l)-1][1]*"0")
