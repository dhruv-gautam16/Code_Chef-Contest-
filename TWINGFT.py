for _ in range(int(input())):
    
    n, k = map(int, input().split(' '))
   
    a = list(map(int, input().split(' ')))
   
    chef_goes = a.copy()
   
    chef1 = chef2 = 0
    i = 0
    moves = 2*k
   
    while i <= moves-1:
        maxi = max(chef_goes)
        ind = chef_goes.index(maxi)
        
        if i%2 == 0:
            chef1 += chef_goes.pop(ind)
        else:
            chef2 += chef_goes.pop(ind)
        
        i += 1   
        
    chef2 += max(chef_goes)
    print(max(chef1, chef2))