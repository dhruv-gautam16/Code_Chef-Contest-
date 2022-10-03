def li(): return list(map(int,input().split())); 
def si(): return input().split()
def ii(): return int(input())
def ip(): return input()
def pow(a,b):
    ans=1; inf=1000000007; 
    while(b>0):
        if(b & 1):
            ans=(ans*a)%inf; 
        a=(a*a)%inf; 
        b>>=1; 
    return ans; 
for tastcas in range(int(input())):
    n,w=li(); inf=1000000007; 
    if(w>=-9 and w<=8):
        c=0; 
        for d1 in range(1,10):
            for d2 in range(0,10):
                if(d2-d1==w): c+=1; 
        print((c*pow(10,n-2))%inf)
    else: print(0)