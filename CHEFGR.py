T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    L = list(map(int,input().split()))
    a = max(L)
    s = sum(L)
    found = False
    while (n*a)-s <= m:
        if (n*a) - s == m:
            found = True
            break
        else:
            a += 1
            
    if found:
        print("Yes")
    else:
        print("No")