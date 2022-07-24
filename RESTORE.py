# cook your dish here
# cook your dish here
# cook your dish here
p_a=[True]*(4*10**6+1)
p_a[0]=False
p_a[1]=False
for l in range(2,4*10**6+1):
    if p_a[l]==True:
        k=2
        while(l*k<=4*10**6):
            p_a[l*k]=False
            k=k+1
li=[]
for l in range(2,4*10**6+1):
    if p_a[l]==True:
        li.append(l)
for _ in range(int(input())):
    n=int(input())
    arr=[int(a) for a in input().split()]
    res=[-1]*n
    i=0
    for l in range(n-1):
        if res[l]!=-1:
            continue
        if arr[l]==l+1:
            res[l]=li[i]
        elif res[arr[l]-1]==-1:
            res[l]=li[i]
            res[arr[l]-1]=li[i]
        elif res[arr[l]-1]!=-1:
            res[l]=res[arr[l]-1]
        i=i+1
    if res[-1]==-1:
        res[-1]=li[i]
    print(*res)
