for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    count = 0
    a.sort()
    flag = 0
    for i in range(n):
        if a[i]>i+1:
            flag = 1
            break
        else:
            count+=a[i]-(i+1)
            
    if flag or count&1==0:
        print('Second')
    else:
        print('First')