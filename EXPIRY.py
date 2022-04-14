for t in range(int(input())):
    n,m,k=map(int,input().split())
    if m*k>=n:
        print("Yes")
    else:
        print("No")