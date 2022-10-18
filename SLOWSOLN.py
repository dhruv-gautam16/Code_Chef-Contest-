# cook your dish here
for _ in range(int(input())):
    t,n,m=map(int,input().split())
    x=m//n
    rem=m%n
    if x+1<=t:
        tot=(n**2)*x+rem**2
    else:
        tot=(n**2)*t
    print(tot)