for i in range(int(input())):
    N,M,K = map(int,input().split())
    sum = 0
    arr = list(map(int,input().split()))
    if 0 not in arr:
        print("100")
        
        
    else:
        for i in range(M):
            sum = sum + arr[i]
            
        if sum == M:
            print(K)
        else:
            print("0")
           