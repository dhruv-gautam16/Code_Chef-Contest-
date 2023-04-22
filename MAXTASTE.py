t=int(input())
for i in range(t):
    A,B,C,D=map(int,input().split())
    M=max(A,B)
    N=max(C,D)
    print(M+N)