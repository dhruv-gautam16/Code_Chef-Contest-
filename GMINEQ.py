for testcases in range(int(input())):
    a=int(input())
    lst=list(map(int,input().split()))
    m=lst.count(-1)
    p=lst.count(1)
    c=abs(m-p)
    if c<2:
        print("YES")
    elif c==2:
        if p%2==0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    