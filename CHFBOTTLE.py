for t in range(int(input())):
    (a,b,c)=map(int,input().split())
    #d=list(map(int,input().split()))
    d=int(c/b)
    if d>a:
        print(a)
    else:
        print(d)

