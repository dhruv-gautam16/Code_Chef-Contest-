# cook your dish here
for _ in range(int(input())):
    n,m,x = map(int,input().split())
    a = [int(x) for x in input().split()]
    players = [(x,i+1) for i,x in enumerate(a)]
    
    ans = []
    for v,i in  sorted(players,reverse=True):
        if len(ans)<x or v>= m:
            ans.append(i)
    
    print(len(ans), *sorted(ans))
    
        
        
        
        
        
            