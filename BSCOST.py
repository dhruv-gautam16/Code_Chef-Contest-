for _ in range(int(input())):
    n, x, y = input().split()
    s = input()
    
    if s.count('01') == 0 and s.count('10') == 0:
        print(0)
    elif int(x) > int(y):
        print(y)
    else:
        print(x)