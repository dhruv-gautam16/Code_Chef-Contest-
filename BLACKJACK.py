for i in range(int(input())):
    a,b=map(int,input().split())
    if(a+b>=11):
        print(21-(a+b))
    else:
        print(-1)