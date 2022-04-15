T = int(input())
for charan in range(T):
    N = int(input())
    if((N-0)%4 ==0):
        print(N+3)
    elif((N-1)%4 ==0):
        print(N)
    elif((N-2)%4 ==0 or (N-3)%4 ==0):
        print(3)
