import sys
import math

long = float(input().replace(',', '.'))
lati = float(input().replace(',', '.'))
n = int(input())

shorter = ""
min = sys.maxsize
for i in range(n):
    raw = input().split(';')

    name = raw[1]
    raw_long = float(raw[-2].replace(',', '.'))
    raw_lati = float(raw[-1].replace(',', '.'))

    x = (raw_long - long) * math.cos(long + raw_long/2)
    y = (raw_lati - lati)
    d = math.sqrt(x**2 + y**2)*6371

    if d < min:
        min = d
        shorter = name

print(shorter)
