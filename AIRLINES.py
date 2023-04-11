T=int(input())
for i in range(T):
    X,Y,Z=map(int,input().split())
    X=X*10
    if(Y<=X):
        print(Y*Z)
    else:
        print(X*Z)