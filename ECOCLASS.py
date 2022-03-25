n=int(input())
for i in range(n):
    a=int(input())
    s=list(map(int,input().split()))
    d=list(map(int,input().split()))
    c=0
    for j in range(0,a):
        if s[j]==d[j]:
            c+=1
    print(c) 