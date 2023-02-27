for i in range(int(input())):
    n=int(input())
    r,s=0,0
    a=list(map(int,input().split()))
    for i in a:
        if i>0:
            r+=1
        else:
            s+=1 
    if s==0:
        s=r
    print(r,s)