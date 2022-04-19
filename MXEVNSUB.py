for _ in range(int(input())):
    n=int(input())
    s=(n*(n+1))//2
    if s%2==0:
        print(n)
    else:
        print(n-1)