import math 
  
# Function to find the largest subset possible  

  
try:
    T = int(input())
    result = 1
    
    for l in range(T):
        n = int(input())
        path = [int(i) for i in input().strip().split(" ")]
        path.sort(reverse = True)
        d = {}
        for i in path:
            d[i] = d.get(i,0)+1
        count = 0    
        for i in d:
            if d[i] >= 1:
                count += 1
        print(count)
            
        
        
            
                
            
            
        
        
        
        
            
            
            
            
except EOFError:
    pass



