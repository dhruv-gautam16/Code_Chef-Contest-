t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    res = 0
    for e in a:
        res |= e
        
    print(bin(res).count("1"))