t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    one = A.count(1)
    ans = True
    if A[0]!=B[0] or A[-1]!=B[-1]:
        ans = False
    else:
        for i in range(1,n-1):
            if A[i]!=B[i]:
                if B[i]==0:
                    ans = False
                    break
                if not one:
                    ans = False
                    break
    print("YES" if ans else "NO")