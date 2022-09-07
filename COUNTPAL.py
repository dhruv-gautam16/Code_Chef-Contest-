# cook your dish here
s=input()
l=len(s)
d=[1]
ans=0
for i in range(1,l):
    ans=0
    for j in range(i+1):
        m=s[j:i+1]
        if m[::-1]==m:
            x=d[j-1]
            if j-1<0:
                x=1
            ans+=x
    d.append(ans)
print(d[-1]%((10**9)+7))