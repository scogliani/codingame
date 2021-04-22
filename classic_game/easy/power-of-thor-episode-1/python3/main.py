import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def taxiDist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def euclidDist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# LX: the X position of the light of power
# LY: the Y position of the light of power
# TX: Thor's starting X position
# TY: Thor's starting Y position
LX, LY, TX, TY = [int(i) for i in input().split()]

L = [LX, LY]
T = [TX, TY]
move = []

while (T != L):
    if euclidDist(T, L) >= taxiDist(T, L):
        if T[0] < L[0]:
            move.append("E")
            T[0] += 1            
        elif T[0] > L[0]:
            move.append("W")
            T[0] -= 1
        
        if T[1] > L[1]:
            move.append("N")
            T[1] -= 1            
        elif T[1] < L[1]:
            move.append("S")
            T[1] += 1
    else:
        if T[0] < L[0]:
            if T[1] > L[1]:
                move.append("NE")
                T[0] += 1
                T[1] -= 1
            elif T[1] < L[1]:
                move.append("SE")
                T[0] += 1
                T[1] += 1

        elif T[0] > L[0]:
            if T[1] > L[1]:
                move.append("NW")
                T[0] += 1
                T[1] -= 1
            elif T[1] < L[1]:
                move.append("SW")
                T[0] += 1
                T[1] += 1

# game loop
while 1:
    #  The level of Thor's remaining energy, representing the number of moves he can still make.
    E = int(input())
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(move.pop(0))
