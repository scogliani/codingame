while 1:
    # name of enemy 1
    enemy_1 = input()

    # distance to enemy 1
    dist_1 = int(input())

    # name of enemy 2
    enemy_2 = input()

    # distance to enemy 2
    dist_2 = int(input())

    # Write an action using print

    # Enter the code here

    print(enemy_1 if dist_1 < dist_2 else enemy_2)
