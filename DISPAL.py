# cook your dish here
t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    if n<(2*x-1):
        print(-1)
    else:
        ans=['a' for i in range(n)]
        for i in range(1,x):
            ans[i-1]=chr(ord('a')+i)
            ans[n-i]=chr(ord('a')+i)
        print(''.join(ans))