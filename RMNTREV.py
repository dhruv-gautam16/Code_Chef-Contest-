
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    x=s[:k]
    y=s[k:]
    r=""
    for i in range(len(x)//2):
        r+=x[i]
        r+=x[-(i+1)]
    if(len(x)%2):
        r+=x[len(x)//2]
    r=r[::-1]
    print(r+y)