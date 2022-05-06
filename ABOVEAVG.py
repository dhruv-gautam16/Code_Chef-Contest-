for i in range(int(input())):
    A,B,C=map(int,input().split())
    d1 = A*C
    d2 = C+1
    if d2>B:
        print(0)
    else:
        print(d1//d2)