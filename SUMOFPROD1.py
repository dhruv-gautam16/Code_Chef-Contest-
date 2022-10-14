for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    s,c=0,0
    for i in a:
        if i==1:
            c+=1 
            s+=c 
        else:
            c=0
    print(s)