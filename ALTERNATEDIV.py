# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n%2 == 0:
        k = n//2
        ans = []
        for i in range(1,k+1):
            o = 2*i - 1 
            ans.append(o)
            ans.append(2*o)
        print(*ans)
    else:
        k = n//2 + 1 
        ans = []
        for i in range(1,k+1):
            o = 2*i - 1 
            ans.append(o)
            ans.append(2*o)
        print(*ans[:-1])