for i in range(int(input())):
    N,M,K = map(int,input().split())
    s = 0
    count = 0
    tra = list(map(int,input().split()))
    ign = list(map(int,input().split()))
    
    for i in range(M):
        for j in range(K):
            if tra[i] == ign[j]:
                count += 1
                
    for i in range(1,N+1):
        if i  not in tra and i not in ign:
            s += 1 
            
    print(count,s)
    
