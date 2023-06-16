t = int(input())
if(t >= 1 and t <= 100):
    for _ in range(t):
        l, r = map(int, input().split())
        c = 0
        if l >= 1 and l <= r and r <= (pow(10, 5)):
            for i in range(l, r+1, 1):
                if i%10==2 or i%10==3 or i%10==9:
                    c+=1
            print(c)
