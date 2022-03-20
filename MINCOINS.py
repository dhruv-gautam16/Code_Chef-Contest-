for i in range(int(input())):
    n=int(input())
    c=0
    if n%5==0:
        c=n//10
        if n%10==5:
            c+=1
        print(c)
    else:
        print(-1)