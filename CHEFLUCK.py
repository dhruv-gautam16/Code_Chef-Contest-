for _ in range(int(input())):
    n = int(input())
    f = 0
    for i in range(7):
        if (n - i * 4) < 0:
            break  
        if (n - i * 4) % 7 == 0:
            f = 1 
            print(n - i * 4)
            break
    if not f :
        print(-1)
