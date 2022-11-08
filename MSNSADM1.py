# cook your dish here
t=int(input())
while t!=0:
    n=int(input())
    s=list(map(int,input().split()))
    f=list(map(int,input().split()))
    m=0
    for j in range(0,n):
        scr=20*s[j]-f[j]*10
        if scr>m:
            m=scr
    print(m)
    t-=1