# cook your dish here
T=int(input())
for i in range(T):
    X,Y,M =list(map(int,input().split()))
    a=X*M
    if (a<Y):
        print("YES")
    else:
        print("NO")
