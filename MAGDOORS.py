# cook your dish here
t=int(input())
for i in range(t):
    s=input()
    ans=0
    r="0"
    for x in s:
        if x==r:
            ans=ans+1
            r='1' if (r=='0') else '0'
    print(ans)
            