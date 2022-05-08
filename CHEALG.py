# cook your dish here
t=int(input())
for j in range(t):
    s=input()
    r=''
    c=1
    for i in range(1,len(s)):
        if(s[i-1]==s[i]):
            c+=1
        else:
            r+=s[i-1]+str(c)
            c=1
    r+=s[-1]+str(c)
    if(len(r)<len(s)):
        print('YES')
    else:
        print('NO')