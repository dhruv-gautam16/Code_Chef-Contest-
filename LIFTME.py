# cook your dish here
t=int(input())
l=list()
for _ in range(t):
    N,Q=map(int,input().split())
    current=0
    total=0
    for _ in range(Q):
        f,d=map(int,input().split())
        
        total+=abs(current-f)
        current=f
        total+=abs(current-d)
        current=d
    l.append(total)
for i in l:
    print(i)