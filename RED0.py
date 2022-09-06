# cook your dish here
t = int(input())

for i in range(t):
    
    x, y = map(int, input().split())
    
    if x > y:
        x, y = y, x
        
    if x == 0 and y == 0:
        print(0)
    
    elif x == 0:
        print(-1)
    
    else:
        steps = 0
        while x < y:
            x *= 2
            steps += 1
        
        print(steps+y)