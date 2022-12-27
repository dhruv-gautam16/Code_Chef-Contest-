# cook your dish here
# cook your dish here
T = int(input())
for tc in range(T):
    # n=days normal year. m=days+ Mob year. k=Mob year, x=Integer
    n,m,k,x = map(int, input().split())
    
    mobYear = n*k + m
    
    x = x % mobYear
    
    if x == 0:
        print('YES')
    elif x <= n*(k-1):
        print('NO')
    elif x <= mobYear:
        print('YES')
    
