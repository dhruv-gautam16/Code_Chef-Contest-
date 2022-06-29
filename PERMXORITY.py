
sl=int(input())
while(sl):
    sl-=1
    n=int(input())
    if n==2:
        print(-1)
    elif n==4:
        print(4,1,3,2)
    else:
        if n%2==1:
            for i in range(n):
                print(i+1,end=" ")
            print()
        else:
            for i in range(n-4):
                print(n-i,end=" ")
            print(4,1,3,2)
            