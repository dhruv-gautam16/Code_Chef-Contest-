for _ in range(int(input())):
    n,k=map(int,input().split())
    x=list(map(int,input().split()))
    s=0
    for i in x:
        s+= i 
    if s%k==0:
        print("0")
    else :
        print("1")

