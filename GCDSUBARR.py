# cook your dish here
for _ in range(int(input())):
    nog,kou=map(int,input().split())
    vok=nog*(nog+1)//2-1
    if(kou<nog*(nog-1)):
        print(-1)
    else:
        for m in range(nog-1):
            print("1 ",end="")
        print(kou-vok)