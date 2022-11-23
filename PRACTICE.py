# cook your dish here
# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    d=(n+k)//2
    a.sort()
    print(a[d])
    
