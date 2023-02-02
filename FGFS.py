from collections import defaultdict
for _ in range(int(input())):
    n, k = map(int, input().split())
    dine_area = defaultdict(list)
    for customer in range(n):
        s, e, pref = map(int, input().split())
        dine_area[pref].append((s, e))
    
   
    def process(dine):
        
        interval = dine_area[dine]
        interval.sort(key = lambda x: x[1])
       
        customers = 1
        prev_end = interval[0][1]
        
        for s, e in interval[1:]:
            
            if s >= prev_end:
                prev_end = e
                customers += 1
               
        return customers
                
           
    total_customers = 0    
    for dine in dine_area:
        total_customers += process(dine)
        
    print(total_customers)
        
