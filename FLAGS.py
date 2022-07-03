
T = int(input())
for _ in range(T):
    N = int(input())
    
    way1 = N*(N-1)*(N-1)
    way2 = N*(N-1)*(N-1)
    way3 = N*(N-1)*(N-2)
    way4 = N*(N-1)*(N-2)*(N-2)
    way5 = N*(N-1)*(N-2)*(N-2)
    
    ans = way1 + way2 + way3 + way4 + way5
    
    print(ans)