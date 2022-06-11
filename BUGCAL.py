for t in range(int(input())):
    a,b=map(int,input().split())
    ans=0
    count=0
    while a>0 or b>0:
        r=(a%10 + b%10)%10
        a=a//10
        b=b//10
        ans=r*(10**count)+ans
        count+=1
        
    print(ans)
