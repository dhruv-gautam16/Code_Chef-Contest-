# PAIR PAIN : PAIRPAIN
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c1 = 0 
    ans = 0
    for i in range(n):
        if l[i] != 1:
            ans += c1 
        else:
            ans += i 
            c1 += 1
    c2 = 0
    for i in range(n):
        if l[i] == 2:
            ans += c2 
            c2 += 1
    print(ans)