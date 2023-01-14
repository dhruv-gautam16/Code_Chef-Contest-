# cook your dish here
mat = {
    (0, 0, 0): 1,
    (0, 0, 1): 0,
    (0, 1, 0): 0,
    (0, 1, 1): 1,
    (1, 0, 0): 0,
    (1, 0, 1): 1,
    (1, 1, 0): 1,
    (1, 1, 1): 4
}
t = int(input())
for _ in range(t):
    p,q,r = list(map(int,input().split()))
    ans = 1 
    while p or q or r:
        x = p % 2
        y = q % 2
        z = r % 2
        ans *= mat[(x, y, z)]
        p //= 2
        q //= 2
        r //= 2
        
    print(ans)