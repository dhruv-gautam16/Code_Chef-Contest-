# cook your dish here
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    if d/b > c/a :
        print(-1)
    elif d/b < c/a:
        print(1)
    else:
        print(0)