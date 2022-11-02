for t in range(int(input())):
        n,m=map(int,input().split())
        x=int(n//2) + n%2
        y=int(m//2) + m%2
        print(x*y)