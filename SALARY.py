for _ in range(int(input())):
    n=int(input())
    w=list(map(int,input().split()))
    print(sum(w)-(n*min(w)))