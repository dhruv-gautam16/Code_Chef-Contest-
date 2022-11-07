# cook your dish here
testcases = int(input())
for i in range(testcases):
    X1 , X2 = map(int ,input().split())
    if(X1 == X2 ):
        print("YES")
    elif(X1 < X2 ):
        print("NO")
    else:
        print("YES")