t = int(input())
for _ in range(t):
    a,b,c,d,k = map(int,input().split())
    p = abs(a-c) + abs(b-d)
    
    if k>=p and (k-p)%2 == 0 :
        print('YES')
    else:
        print('NO')