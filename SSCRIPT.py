for i in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    c=0
    flag=False
    for i in s:
        if i=="*":
            c=c+1
            if c>=k:
                flag=True
                break
        else:
            c=0
            
    if flag==True:
        print("YES")
    else:
        print("NO")