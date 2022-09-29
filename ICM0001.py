t=int(input())
for i in range(0,t):
    n=int(input())
    a=list(map(int, input().split()))
    x=a[0]
    flag=0
    ind=0
    for j in range(1,n):
        if a[j]-a[j-1]<0:
            ind=j
            flag+=1
    if flag==1:
        for k in range(ind,n):
            if a[k]>x:
                flag=2
                break
        if flag==2:
            print("No")
        else:
            print("Yes")
            print(1)
    elif flag>1:
        print("No")
    else:
        print("Yes")
        print(0)