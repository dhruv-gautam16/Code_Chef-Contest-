# cook your dish here
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    l1 = [int(x) for x in input().split()]
    l2 = [int(x) for x in input().split()]
    a,b = [],[]
    ans = []
    mx = 0
    for i in range(n):
        if mx<=abs(l2[i]):
            mx = abs(l2[i])
            ans = [l1[i],l2[i],i]
    res = 0
    # print(ans,mx)
    if (ans[0]>=0 and ans[1]>=0):
        res = (ans[0]+k)*ans[1]
    elif (ans[0]<0 and ans[1]<0):
        res = (ans[0]-k)*ans[1]
    else:
        # print("rehan")
        if ans[0]<0:
            res = (ans[0]+k)*ans[1] 
        else:
            res = (ans[0]-k)*ans[1]
    # print(ans)
    for i in range(n):
        if i==ans[2]:
            continue
        else:
            res += (l1[i]*l2[i])
    print(res)