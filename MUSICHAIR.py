# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    x = n-1 
    i = 1 
    count = 0 
    
    while i*i <=x:
        if x%i ==0:
            count +=1 
            
            if x//i !=i:
                count +=1 
        i = i+1 
    print(count)