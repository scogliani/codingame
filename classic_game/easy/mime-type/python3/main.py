dict = {}
N = int(input())
Q = int(input())

for i in range(N):
    raw = input().split()
    dict.update({raw[0].lower():raw[1]})

for i in range(Q):
    try:
        raw = input().split('.')
        if len(raw) > 1:
            print(dict[raw[-1].lower()])
        else:
            print("UNKNOWN")
    except KeyError:
        print("UNKNOWN")
