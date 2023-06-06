for _testcase in range(int(input())):
    a,b = map(int, input().split())
    c = list(map(int,input().split()))
    d = list(map(int,input().split()))
    count = 0
    for i in range(a):
        if (c[i]) >= b:
            count += (d[i])
    
    print(count)
        
