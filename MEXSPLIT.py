from collections import Counter

for _ in range (int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    d=Counter(l)
    print(max(d[0],n-d[0]))