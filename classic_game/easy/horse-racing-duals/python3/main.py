import sys

n = int(input())

l = []
for i in range(n):
    l.append(int(input()))
    
l.sort()
min = sys.maxsize
for i in range(-1, len(l)-1):
    if abs(l[i]-l[i+1]) < min:
        min = abs(l[i]-l[i+1])
print(min)