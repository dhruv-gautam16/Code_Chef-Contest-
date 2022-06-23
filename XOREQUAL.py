# cook your dish here
n = int(input())

mt = 100000
mx = 1000000007
ar = [0 for i in range(mt+1)]
ar[1] = 1
for i in range(2,mt+1):
    ar[i] = (ar[i-1]*2)%mx
for _ in range(n):
    m = int(input())
    print(ar[m])