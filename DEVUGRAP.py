# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for i in l:
        if i<=b:
            c+=(b-i)
        else:
            c+=min(i%b,b-(i%b))
    print(c)
        