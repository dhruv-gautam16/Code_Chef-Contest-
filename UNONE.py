t = int(input())
for tests in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    res = []
    for i in range(len(a)):
        if a[i]%2==0:
            res.append(a[i])    
    for i in range(len(a)):
        if a[i]%2!=0:
            res.append(a[i])
    for i in range(len(res)):
        print(res[i],end = " ")
    print()