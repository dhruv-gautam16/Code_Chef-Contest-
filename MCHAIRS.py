# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    mod = 1000000007
    print((pow(2, n, mod)-1) % mod)
        
        
    
