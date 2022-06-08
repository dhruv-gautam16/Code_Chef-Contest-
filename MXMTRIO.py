# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    a=max(l1)
    b=min(l1)
    l1.sort()
    c=l1[-2]
    print((a-b)*c)
