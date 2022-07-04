fptr = open(0)

for _ in range(int(next(fptr))):
    
    N = int(next(fptr))
    
    a = [1, 3, 4, 2]
    
    if N == 3:
        print(-1)
    
    elif N == 4:
        print(1, 3, 4, 2)
    
    else:
        for i in range(N):
            if i < 4:
                print(a[i], end = ' ')
                
            elif i != N - 1:
                print(i + 1, end = ' ')
                
            else:
                print(N)