# cook your dish here
t = int(input())

for _ in range(t):
    
    n, k, v = map(int, input().split())
    
    a = list(map(int, input().split()))
    
    foo = ((v * (n + k)) - (sum(a)))
    x = ((v * (n + k)) - (sum(a))) // k 
    
    if x > 0 and (foo % k) == 0:
        
        print(x)
        
    else:
        
        print(-1)