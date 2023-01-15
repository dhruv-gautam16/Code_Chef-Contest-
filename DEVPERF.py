# cook your dish here
t=int(input())
for j in range(t):
    n,m=list(map(int,input().split()))
    arr=[]
    for i in range(n):
        arr.append(input())
    l1=[]
    l2=[]
    for i in range(n):
        for k in range(m):
            if arr[i][k]=='*':
                l1.append(i)
                l2.append(k)
        
    if len(l1)==0:
        print(0)
    else:
        x1=max(l1)
        x2=min(l1)
        y1=max(l2)
        y2=min(l2)
        if (x1-x2)%2==1:
            c1=int((x1-x2+1)//2+1)
        else:
            c1=int((x1-x2)//2+1)
        if (y1-y2)%2==1:
            c2=int((y1-y2+1)//2+1)
        else:
            c2=int((y1-y2)//2+1)
        print(max(c1,c2))