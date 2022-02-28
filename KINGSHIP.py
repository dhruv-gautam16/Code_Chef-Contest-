for t in range(int(input())):
    n=int(input())
    d=list(map(int,input().split()))
    e=min(d)
    d.remove(e)
    ans=0
    for i in d:
        ans=ans+(i*e)
    print(ans)
