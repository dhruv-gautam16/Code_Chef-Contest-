# cook your dish here
T=int(input())
for i in range(T):
    X,Y,N,R=map(int,input().split())
    X=int(X)
    Y=int(Y)
    N=int(N)
    R=int(R)
    tY=(R-(X*N))//(Y-X)
    if tY<0:
        print(-1)
    else:
        if N-tY<0:
            print(0,N)
        else:
            print(N-tY,tY)
    