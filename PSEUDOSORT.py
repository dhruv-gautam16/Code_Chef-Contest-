for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if a==sorted(a):
        print("Yes")
    else:
        for i in range(1,len(a)):
            
            if(a[i-1]>a[i]):
                a[i-1],a[i]=a[i],a[i-1]
                break
        if a==sorted(a):
            print("Yes")
        else:
            print("No")