for _ in range(int(input())):
    n,m = map(int, input().split())
    freq = []
    res =[0 for _ in range(m)]
    arr=[]
    for _ in range(m):
        arr.append(list(map(int, input().split())))
    i=m-1
    while i>=0:
    #for i in range(m):
        if arr[i][0] not in freq and arr[i][1] not in freq:
            res[i]=1
            freq += arr[i]
        i-=1
    ans= [i for i in range(m) if res[i]==1]
    print(*ans)