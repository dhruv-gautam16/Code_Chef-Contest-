# cook your dish here
try:
    t = int(input())
    for r in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        b = sorted(a)
        c = 0
        d = (len(b))
        
        for i in range(d):
            if(b[i]!=i+1 and b[i]<i+1):
                c += abs(b[i] - (i+1))
            elif b[i]>i+1:
                c = -1
                break    
            
        print(c) 
        
        
except:
    pass

