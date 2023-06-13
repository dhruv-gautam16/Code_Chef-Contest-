# cook your dish here
for i in range(int(input())):
    x,y,z = map(int, input().split())
    if x+y<z:
        print("PLANEBUS")
    elif x+y==z:
        print("EQUAL")
    else:
        print("TRAIN")