t=int(input())
for i in range(t):
    X,Y=map(int,input().split())
    if(X<Y):
        print("YES")
    else:
        print("NO")
