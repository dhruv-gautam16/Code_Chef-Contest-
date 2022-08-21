

def until_odd(x):
    
    count=0
    
    while x%2==0:
        
        x=x//2
        count+=1
        
    return count
        
def min_count(arr):
    
    min_count = float("inf")
    
    for num in arr:
        min_count = min(min_count,until_odd(num))
            
            
    return min_count
    
    
#print(min_count([3,5]))

def read_out():
    
    T = int(input())
    
    for _ in range(T):
        
        n = int(input())
        
        arr = list(map(int,input().split(" ")))
        
        print(min_count(arr))

read_out()

    
    

        
        
        
        