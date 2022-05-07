# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    l=[0]*101
    for i in range(n):
        a,b=map(int,input().split())
        l[b]+=a
    for j in range(m):
        a,b=map(int,input().split())
        l[b]-=a
    s=0
    for i in l:
        if i<0:
            s+=i
    print(s*-1)
         
        
 
