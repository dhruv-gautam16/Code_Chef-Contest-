# cook your dish here
t=int(input())
for j in range(t):
    n,a,b=map(int,input().split())
    r='EQUINOX'
    u=0
    v=0
    for k in range(n):
        s=input()
        i=s[0]
        if i in r:
            u+=a
        else:
            v+=b
    if(u>v):
        print("SARTHAK")
    elif(v>u):
        print("ANURADHA")
    else:
        print('DRAW')
                
            