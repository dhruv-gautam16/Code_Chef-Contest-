# cook your dish here
mod=10000009
t=int(input())
while(t):
    t=t-1
    s=input()
    i=0
    j=len(s)-1
    c=1
    while(i<=j):
        if s[i]=='?' and s[j]=='?':
            c=c*26%mod
        elif s[i]=='?' or s[j]=='?':
            pass
        elif s[i]!=s[j]:
            c=0
            break
        i=i+1
        j=j-1
        
    print(c%mod)
        
            
            