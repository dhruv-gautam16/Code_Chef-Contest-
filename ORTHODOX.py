
mod=1000000007
read_int = lambda: int(input().strip())
read_str = lambda: input().strip()
read_str_arr = lambda: input().strip().split()
read_int_arr = lambda: [int(x) for x in input().strip().split()]


def solve():
    N = read_int()
    A = read_int_arr()

    seen = set()

    distinct = True
    for i in range(N):
        prev = 0
        for j in range(i, N):
            val = prev | A[j]
            if val in seen:
                distinct = False
                break
            else:
                seen.add(val)
            prev = val
        
        if not distinct:
            break
    
    print('YES' if distinct else 'NO')



for _ in range(int(input())):
    solve()
