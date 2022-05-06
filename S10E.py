# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    t=[]
    ans=0
    for i in l:
        t.append(i)
        if len(t)>6:
            del t[0]
        m=min(t)
        if t[-1]==m and m not in t[:-1]:
            ans+=1
    print(ans)