import sys
import string

alphabet = string.ascii_lowercase+"?"

def displayLetter(L, H, T, letters):
    word = T.lower()
    res = ""
    
    for i in range(H):
        for e in word:
            if not(e in letters):
                e = alphabet[-1]
            res += letters[e][i*L:(i*L)+L]
        res += "\n"
        
    return res

L = int(input())
H = int(input())
T = input()

letters = {}
for i in range(H):
    line = input()

    for j in range(27):
        try:
            letters[alphabet[j]] += line[j*L:(j*L)+L]
        except KeyError:
            letters.update({alphabet[j]:line[j*L:(j*L)+L]})

print (displayLetter(L, H, T, letters))
