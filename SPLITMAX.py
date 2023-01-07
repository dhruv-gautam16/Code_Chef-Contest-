# cook your dish here
for testcases in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    sum,mod=0,998244353;
    for i in a: 
        sum+=i
        sum%=mod 
    
    print(sum*(sum-1)%mod)
    
    