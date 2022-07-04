# cook your dish here
t=int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    arr=list(map(int, input().split()))
    c=0
    x=0
    ar=[0]*(n+1)
    for i in arr:
        ar[i]+=1
    for i in range(k):
        if ar[i]>0:
            c+=1
        else:
            break
    if k<=m and c==k and n-ar[k]>=m:
        print('YES')
    else:
        print('NO')
    