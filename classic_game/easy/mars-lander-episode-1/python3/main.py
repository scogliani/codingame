import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

landing = []
N = int(input()) # the number of points used to draw the surface of Mars.
for i in range(N):
    # LAND_X: X coordinate of a surface point. (0 to 6999)
    # LAND_Y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    LAND_X, LAND_Y = [int(i) for i in input().split()]
    
    if len(landing) < 2:
        if len(landing) != 0:
            if landing[0][1] != LAND_Y:
                landing.pop()
            landing.append([LAND_X, LAND_Y])
            
        else:
            landing.append([LAND_X, LAND_Y])

# game loop
while 1:
    # HS: the horizontal speed (in m/s), can be negative.
    # VS: the vertical speed (in m/s), can be negative.
    # F: the quantity of remaining fuel in liters.
    # R: the rotation angle in degrees (-90 to 90).
    # P: the thrust power (0 to 4).
    X, Y, HS, VS, F, R, P = [int(i) for i in input().split()]
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    if VS < -39:
        print("0 4")
    else:
        print("0 0")# R P. R is the desired rotation angle. P is the desired thrust power.
