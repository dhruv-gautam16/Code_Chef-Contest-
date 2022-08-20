# cook your dish here
def solve():
    a, b = map(int, input().split())
    x, y = map(int, input().split())
    
    s = set()
    for d in [b + 1, b - 1]:
        if d >= 1 and d <= 8:
            for c in [a + 2, a - 2]:
                if c >= 1 and c <= 8:
                    s.add((c, d))
                    
    for d in [b + 2, b - 2]:
        if d >= 1 and d <= 8:
            for c in [a + 1, a - 1]:
                if c >= 1 and c <= 8:
                    s.add((c, d))
                    
    for d in [y + 1, y - 1]:
        if d >= 1 and d <= 8:
            for c in [x + 2, x - 2]:
                if c >= 1 and c <= 8:
                    if (c, d) in s:
                        return "YES"
                        
    for d in [y + 2, y - 2]:
        if d >= 1 and d <= 8:
            for c in [x + 1, x - 1]:
                if c >= 1 and c <= 8:
                    if (c, d) in s:
                        return "YES"
                        
    return "NO"


for _ in range(int(input())):
    print(solve())