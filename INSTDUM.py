t = int(input())
for i in range(t):
    N = int(input())
    A = list(map(int, input().split()))
    
    run = 0
    count = 0
    for i in range(N):
        run += A[i]
        strike_rate = (run / (i + 1)) * 100
        if strike_rate == 100:
            count = count + 1
        
    print(count)