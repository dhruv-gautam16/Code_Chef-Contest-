# cook your dish here
for _ in range(int(input())):
    p = input()
    ph = int(p[:2])
    pm = int(p[3:5])
    pp = p[-2:]
    if pp == "PM":
        pm += 720
    if ph!=12:
        pm += (ph*60)
    
    n = int(input())
    s = ""
    for _ in range(n):
        t = input()
        t1,t2 = t[:9],t[9:]
        
        
        t1h = int(t1[:2])
        t1m = int(t1[3:5])
        t1p = t1[6:8]
        # print(t1h,t1m,t1p)
        if t1p == "PM" :
            t1m += 720
        if t1h!=12:
            t1m += (t1h*60)
            
            
        t2h = int(t2[:2])
        t2m = int(t2[3:5])
        t2p = t2[-2:]
   
        if t2p == "PM" :
            t2m += 720
        if t2h!=12:
            t2m += (t2h*60)
            
        # print(t1h,ph,t2h)
        # print(t1m,pm,t2m)
        if t1m<=pm<=t2m :
            s += "1"
        else:
            s += "0"
    print(s)