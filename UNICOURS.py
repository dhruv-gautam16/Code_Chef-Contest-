t=int(input())
for q in range(t):
    n=int(input())
    l=list(int(i) for i in input().split())
    print(n-max(l))
