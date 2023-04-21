T = int(input())
for _ in range(T):
    n ,x =list(map(int,input().split()))
    count = 0
    l = list(map(int,input().split()))
    for a in l:
        if a >= x:
            count += 1
             
    print(count)
        
        