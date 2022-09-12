for _ in range(int(input())):
    s=input()
    c=0
    n=len(s)
    m=0
    r=n-1
    curr=n-1
    while(curr>=0 and s[r]=='1'):
        curr-=1 
        r-=1 
    while curr>=0:
        if s[curr]=='1':
            if s[curr+1]=='0':
                c+=1 
            m+=c+(r-curr)
            r-=1 
        curr-=1 
    print(m)    