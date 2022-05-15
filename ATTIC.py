# cook your dish here
for _ in range(int(input())):
    s = input().split('#')
    m = 0
    d =0 
    for i in s:
        if i != "":
            if len(i) > m:
                d += 1 
                m = len(i)
    print(d)
                
        
    
