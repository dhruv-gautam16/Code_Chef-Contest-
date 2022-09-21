a=int(input())

while a!=0:
    ans=0
    now=1
    n,m=map(int,input().split())
    f1=list(map(int,input().split()))
    f2=list(map(int,input().split()))
    # 1 is for Football i.e f1
    # 2 is for Cricket i.e f2
    timeline = [(i, 1) for i in f1] + [(i, 2) for i in f2]
    timeline = sorted(timeline)
    for i in timeline:
      if i[1]!=now:
        ans=ans+1
        now=i[1]

    print(ans)
    a=a-1





