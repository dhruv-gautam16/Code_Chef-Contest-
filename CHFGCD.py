# cook your dish here
def kalki(x, y):
    while y:
        x, y = y, x % y
    return x


for t in range(int(input())):
    n1, n2 = [int(z) for z in input().split()]
    if n1 & 1 == 0 and n2 & 1 == 0:
        print(0)
    elif kalki(n1, n2) > 1:
        print(0)
    else:
        if kalki(n1 + 1, n2) > 1:
            print(1)
        elif kalki(n1, n2 + 1) > 1:
            print(1)
        else:
            print(2)
        