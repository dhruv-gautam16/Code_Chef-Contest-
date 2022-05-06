# cook your dish here
t=int(input())
for j in range(t):
    n=int(input())
    g=0
    for i in range(n):
        s,p,v=map(int,input().split())
        if (p//(s+1))*v>g:
            g=(p//(s+1))*v
    print(g)