for _ in range(0, int(input())):
    c = int(input())
    a = []
    low = 1
    high = c
    for i in range(1, c+1):
        if i % 2 == 1:
            a.append(high)
            high-=1
        else:
            a.append(low)
            low+=1
    print(*a)
    
        