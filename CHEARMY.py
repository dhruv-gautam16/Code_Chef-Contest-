# cook
        
for _ in range(int(input())):
    k = int(input())
    k= k-1 
    ans = 0
    mul = 1
    while k:
        ans += (k%5)*2*mul
        k = k//5 
        mul = mul *10
    print(ans)
        
    
        
        