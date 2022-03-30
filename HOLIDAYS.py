# cook your dish here
t=int(input())
for _ in range(t):
    n,w=map(int,input().split())
    a=list(map(int,input().split()))[:n]
    a.sort(reverse=True)
    c,s=0,0
    for i in a:
        s+=i
        c+=1 
        if s>=w:
            break
    print(n-c)    