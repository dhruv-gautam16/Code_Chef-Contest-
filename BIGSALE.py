# cook your dish here
t=int(input())
l=[]
for _ in range(t):
    n=int(input())
    totalLoss=0
    for _ in range(n):
        p,q,d=map(float,input().split())
        a=(p+p*d/100)
        b=(a-a*d/100)
        
        totalLoss+=q*(p-b)
    l.append(totalLoss)
for j in l:
    print(j)