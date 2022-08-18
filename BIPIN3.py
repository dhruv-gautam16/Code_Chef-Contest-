
m = 10**9 + 7

def power(x,n):
    
    if n==0:
        
        return 1
        
    if n==1:
        return x
        
    
    if n%2==0:
        
        return (power(x,n//2)**2)%m
        
    else:
        
        return (x*power(x,(n-1)//2)**2)%m
    


def max_num_ways(n,k):
    
    return  (k*power(k-1,n-1))%m 
    
    
def read_out():
    
    T = int(input())
    
    
    for _ in range(T):
        
        [n,k] = map(int,input().split(" "))
        
        print(max_num_ways(n,k))
        
read_out()
        
        