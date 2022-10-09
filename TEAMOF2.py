for _ in range(int(input())):
    n = int(input())
    X = []
    flag = 0
    for tc in range(n):
        L = list(map(int, input().split()))
        if L[0]==5:
            flag = 25
        elif L[0]==3 or L[0]==4:
            flag += 1
        X.append(L)
    if flag>20:
        print('YES')
    elif flag>0:
        f = False
        for i in range(n):
            if X[i][0]==3 or X[i][0]==4:
                for j in range(n):
                    if (1 in X[i][1:] or 1 in X[j][1:]) and (2 in X[i][1:] or 2 in X[j][1:]) and (3 in X[i][1:] or 3 in X[j][1:]) and (4 in X[i][1:] or 4 in X[j][1:]) and (5 in X[i][1:] or 5 in X[j][1:]):
                        f = True 
                        break
        if f:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
        