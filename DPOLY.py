for i in range(int(input())):
    n=int(input())
    c=list(map(int,input().split()))
    degree=0
    for i in range(len(c)):
        if c[i] != 0 and i>degree:
            degree=i 
    print(degree)