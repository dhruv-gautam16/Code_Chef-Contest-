# cook your dish here
for _ in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    s=set()
    for i in range(a):
        s.add(l[i]-i)
    if len(s)==1:
        print(a)
    else:
        print(1)
    