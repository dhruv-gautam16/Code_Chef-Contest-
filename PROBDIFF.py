# cook your dish here
for _ in range(int(input())):
    a=list(map(int,input().split()))
    n=len(a)
    a.sort()
    if a[0]==a[3]:
        print(0)
    elif a[0]==a[2] or a[1]==a[3]:
        print(1)
    else:
        print(2)