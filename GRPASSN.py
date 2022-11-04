from collections import Counter
for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = Counter(l);
    check=True
    for i in c:
        if c[i]%i != 0:
            check=False
            break
    if(check):
        print("YES")
    else:
        print("NO")
    