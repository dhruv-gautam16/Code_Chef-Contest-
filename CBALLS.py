def primes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return tuple(p for p in range(2, n+1) if prime[p])

gcds = primes(10000)
for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = float('inf')

    for g in gcds:
        balls = curr = 0
        for i in range(n):
            if a[i] > curr:
                curr = ((a[i]+g-1)//g)*g #a[i]+(g-a[i]%g)
            balls += curr-a[i]
        ans = min(ans, balls)
    
    print(ans)

    
