# cook your dish here
for t in range(int(input())):
    a,b,c=map(int,input().split())
    if b==1 and a>1:
        print(-1)
    elif a>b*c:
        print(-1)
    else:
        for i in range(a):
            print((i%b)+1,end=" ")
        print()