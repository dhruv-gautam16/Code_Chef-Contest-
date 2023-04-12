n = int(input())
for _ in range(n):
    r1,r2,r3 = map(int,input().split())
    if r1 > r2+ r3 or r2 > r3+ r1 or r3 > r1 + r2:
        print('yes')
    else:
        print('no')