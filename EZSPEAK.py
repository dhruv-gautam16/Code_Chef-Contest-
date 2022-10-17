# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    a,b=0,0
    for i in range(n):
        if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
            a=0
            continue
        else:
            a+=1
            if(a>=4):
                b=1 
                break
    if(b>=1):
        print('NO')
    else:
        print('YES')