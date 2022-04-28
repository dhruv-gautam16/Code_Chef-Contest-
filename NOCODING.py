t=int(input())
for j in range(t):
    s=list(input())
    sum=0
    for i in range(len(s)-1):
        z=(ord(s[i])-ord(s[i+1]))
        if(z>0):
            x=26-z
            sum+=x
        else:
            sum+=(-z)
    sum+=(len(s)+1)
    y=11*(len(s))
    if(sum<=y):
        print('YES')
    else:
        print('NO')