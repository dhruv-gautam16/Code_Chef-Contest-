for _ in range(int(input())):
    N,X = map(int,input().split())
    f = X-(N-1)
    if X<N:
        print(-1)
    else:
        arr = []
        for j in range(1,N+1):
            arr.append(j)
        arr.remove(f)
        arr.insert(0,f)
        for e in arr:
            print(e,end=" ")
        print("")