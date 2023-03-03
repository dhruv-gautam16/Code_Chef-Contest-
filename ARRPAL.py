for _ in range(int(input())):
    n = int(input())
    S = [int(x) for x in input().split()]
    
    dif = S[-1] - S[0]
    ans = True
    for i in range(int(n/2)):
        if S[-i - 1] - S[i] > dif or S[-i - 1] - S[i] < 0:
            print(-1)
            ans = False
            break
        dif = S[-i - 1] - S[i]
    
    if ans:
        print(S[-1] - S[0])
        
    
