for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m=max(a)
    c=m
    j=0
    while(j<n):
        if a[j]<c:
            c-=1
            j+=1
        else:
            c+=1
            m=m+1
    print(m-1)