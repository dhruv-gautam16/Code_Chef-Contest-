# cook your dish here
for _ in range(int(input())):
    n = int(input())
    def large_pow(n):
        p = 1 
        while p *2 <= n:
            p *= 2 
        return p 
    lp = large_pow(n)
    ans1 = n - lp + 1 
    sp = lp//2
    ans2 = lp -sp 
    print(max(ans1,ans2))
        
    
    
