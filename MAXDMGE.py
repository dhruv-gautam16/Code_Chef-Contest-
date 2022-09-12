# cook your dish here
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    ans=list()
    nm=0
    for i in range(n):
        if i==0:
            nm=lst[0]&lst[1]
        elif i==(n-1):
            nm=lst[i]&lst[i-1]
        else:
            nm=max(lst[i]&lst[i-1],lst[i]&lst[i+1])
        ans.append(nm)
    print(*ans)