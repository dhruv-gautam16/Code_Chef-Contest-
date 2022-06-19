# from sys import stdin
def map_(l):
    
    for i in range (len(l)-1,0,-1):
        if l[i]>0:
            return i+1
            
        
t=int(input())
for i in range (t):
    ar=list(map(int,input().split()))
    n=int(input())
    i=len(ar)-1
    while  (ar[i]<=n):
        if ar[i]<=n:
            n=abs(ar[i]-n)
            # ar[i]=0
            i-=1 
        else:
            i-=1
            
    print(i+1)
    
            
        