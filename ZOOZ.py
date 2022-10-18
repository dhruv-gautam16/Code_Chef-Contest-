# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    res=[]
    if(n%2==1):
        pair=(n-1)//2
        for w in range(pair):
            res.append('01')
        res.append('0')
    else:
        pair=n-4
        res.append("10")
        for w in range(pair):
            res.append('0')
        res.append("01")
    print("".join(res))
        