for t in range(int(input())):
    a=list(map(int,input().split()))
    i=0
    j=0
    for k in range(len(a)):
        if(a[k]==1):
            i=i+1
        else:
            j=j+1
    if(i<j):
        print("NO")
    else:
        print("YES")