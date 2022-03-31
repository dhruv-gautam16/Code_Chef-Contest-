for _ in range(int(input())):
    h,p=map(int,input().split())
    if h<2*p:
        print(1)
    else:
        print(0)