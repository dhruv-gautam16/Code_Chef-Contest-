t = int(raw_input())
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
while t:
    t-=1 
    r,c = map(int ,raw_input().split())
    grid = [raw_input() for _ in xrange(r)]
    ans = [[float('inf')] * c for _ in xrange(r)]
    for i in xrange(r):
        block = 0 
        for j in xrange(c):
            if grid[i][j] == '^':
                ans[i][j] = min(ans[i][j], block) 
                block += 1 
            else:
                block = 0 
    for i in xrange(r):
        block = 0 
        for j in xrange(c-1, -1, -1):
            if grid[i][j] == '^':
                ans[i][j] = min(ans[i][j], block) 
                block += 1 
            else:
                block = 0 
    for j in xrange(c):
        block = 0 
        for i in xrange(r):
            if grid[i][j] == '^':
                ans[i][j] = min(ans[i][j], block) 
                block += 1 
            else:
                block = 0 
    for j in xrange(c):
        block = 0 
        for i in xrange(r-1, -1, -1):
            if grid[i][j] == '^':
                ans[i][j] = min(ans[i][j], block) 
                block += 1 
            else:
                block = 0 
    q = 0
    from bisect import bisect
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '^':
                q += bisect(primes, ans[i][j]) 
    print q