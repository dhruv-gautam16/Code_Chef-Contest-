# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    time = 0
    charging = False
    
    while n != 50:
        if n < 50 and not charging:
            charging = True
        elif n > 50 and charging:
            charging = False
        n += 2 if charging else -3
        time += 1
        
    print(time)
