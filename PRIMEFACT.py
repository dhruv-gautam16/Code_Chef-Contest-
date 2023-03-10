import math as M
t = int(input())
for _ in range(t):
    x,y = list(map(int,input().split()))
    need = y - x
    if x%2==0:
        print(int(M.ceil(need/2)))
    else:
        if x==9:
            need -= 3
            print(int(M.ceil(need/2))+1)
        else:
            need -= x
            print(int(M.ceil(need/2))+1)
        
        
        