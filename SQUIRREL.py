# cook your dish here
def binary_search():
    l = 0
    r = 10**9+101
    res = 0
    while(l<=r):
        Sum = [0]*m
        mid = (l+r)//2
        for i in range(m):
            Sum[i] = max((mid - t[i])//p[i]+1,0)
        Sum.sort(reverse = True)
        x = sum(Sum[0:(n)])
        if x>=k:
            r = mid -1
            res = mid
        else:
            l = mid+1
    return res
for i in range(int(input())):
    m,n,k = map(int,input().split())
    t = list(map(int,input().split()))
    p = list(map(int,input().split()))
    print(binary_search())