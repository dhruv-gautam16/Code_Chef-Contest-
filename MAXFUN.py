T=int(input())
for t in range(T):
    N=int(input())
    A=list(map(int,input().split(' ')))
    A.sort()
    x=A[-1]
    y=A[0]
    z=A[1]
    c=abs(x-y)+abs(y-z)+abs(z-x)
    print(c)
