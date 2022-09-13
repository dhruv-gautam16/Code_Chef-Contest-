
mod=1000000007
read_int = lambda: int(input().strip())
read_str = lambda: input().strip()
read_str_arr = lambda: input().strip().split()
read_int_arr = lambda: [int(x) for x in input().strip().split()]


def solve():
    a,b = read_int_arr()

    if a==b:
        print(-1)
        return
    
    n = abs(a-b)

    # ans = count of factors of |a-b|
    ans = 0
    i = 1

    while i*i <= n:
        if n % i == 0:
            ans+=1
            if i != n/i:
                ans += 1
        i+=1
    
    print(ans)





for _ in range(int(input())):
    solve()
