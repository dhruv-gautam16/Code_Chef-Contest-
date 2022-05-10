# cook your dish here
t=int(input())
for j in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ct=0
    z=a.count(2)
    y=a.count(0)
    r=(z*(z-1))//2+(y*(y-1))//2
    print(r)
    
    
            