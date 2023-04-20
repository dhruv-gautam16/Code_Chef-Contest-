t = int(input())
for i in range(t):
    x,y,z = map(int, input().split())
    if (z%x == 0 and z%y != 0):
        print("CHICKEN")
    elif (z%y == 0 and z%x != 0):
        print("DUCK")
    elif (z%x == 0 and z%y == 0):
        print("ANY")
    else:
        print("NONE")