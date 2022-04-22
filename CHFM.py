for tc in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x=sum(a)
    mean=x//n
    if mean*n==x:
        if mean in a:
            print(a.index(mean)+1)
        else:
            print("Impossible")
    else:
        print("Impossible")