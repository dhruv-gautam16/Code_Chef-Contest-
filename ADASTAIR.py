# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    steps = list(map(int, input().split()))
    
    steps_to_add = 0
    ada_height = 0
    
    if max(steps) <= k:
        print(0)
        
    else:
        for step in steps:
            jump = step - ada_height
            if jump > k:
                steps_to_add += (jump-1)//k
            ada_height = step
            
        print(steps_to_add)