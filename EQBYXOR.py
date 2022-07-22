# cook your dish here
for _ in range(int(input())):
    a, b, n=map(int, input().split())
    if a==b:
        print(0)
    else:
        c=1 
        while c<n:
            c*=2 
        if a^b<n:
            print(1)
        elif a^b<c:
            print(2)
        else:
            print(-1)