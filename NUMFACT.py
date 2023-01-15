# cook your dish here
# cook your dish here
from collections import defaultdict
def get_primes():
    n = 10**6
    
    is_prime = [True]*(n+1)
    res = []
    i = 2
    while i <= n:
        if is_prime[i]:
            j = 2*i 
            while j <=n:
                is_prime[j] = False
                j += i 
            
            res.append(i)
        
        i += 1
    
    return res
         
t = int(input())
primes = get_primes()
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    d = defaultdict(int)
    for ele in arr:
        for p in primes:
            while ele % p == 0 and ele != 1:
                ele //=p
                d[p] += 1
            
            if ele == 1:
                break 
    
    res = 1
    for ele in d:
        if ele == 1:
            continue
        res *= d[ele] + 1 

    print(res)