for _ in range(int(input())):
    n,k = map(int,input().split())
    y=list(map(int,input().split()))
    c = 0
    for i in y:
        if i >1:
            c+=1
    if c<=k:
        print("YES")
    else :    
        print("NO") 
