m = 100000007
T = int(input())
for t in range(T):
    N = int(input())
    i = (m+1)//2
    R1 = (((pow(3,N,m) + 1) * i) - pow(2,N,m)) % m
    R2 = (pow(2,2*N-1,m) + pow(2,N-1,m) - pow(3,N,m) - R1) % m
    print(R1, R2)