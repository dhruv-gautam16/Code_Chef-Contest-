t=int(input())
while(t>0):
    a,b,c=map(int,input().split())
    d=(a*b)
    e=(a+c)
    f=min(d,e)
    print(f)
    t-=1
    
