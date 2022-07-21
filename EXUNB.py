# cook your dish here
t=int(input())
for j in range(t):
    n=int(input())
    if n%2==0:
        print('NO')
    else:
        p=n//2
        q='1'*p+'0'*(n-p)
        print('YES')
        for i in range(1,n+1):
            print(q[n-i:]+q[:n-i])