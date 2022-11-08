# cook your dish here
t=int(input())
while t!=0:
    s=input()
    u=0
    d=0
    l=len(s)
    for k in range(1,l):
        if s[k]!=s[k-1]:
            if s[k]=="U":
                d+=1
            else:
                u+=1 
    if s[l-1]=="U":
        u+=1 
    else:
        d+=1
    print(min(u,d))
    t-=1