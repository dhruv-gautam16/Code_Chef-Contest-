# cook your dish here
n = int(input())
c = list(map(int,input().split()))
s = sum(c)
if s == n * (n + 1) // 2:
    print("YES")
else:
    print("NO")