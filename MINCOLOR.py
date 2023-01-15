def solve(n, m, x1, y1, x2, y2):
    one_parity = (x1+y1) % 2
    two_parity = (x2+y2) % 2
    first_color = 1
    second_color = 2 if one_parity != two_parity else 3
    for x in range(n):
        for y in range(m):
            parity = (x+y) % 2
            if (x,y) == (x1,y1):
                color = 1
            elif (x,y) == (x2,y2):
                color = 2
            elif parity == one_parity:
                color = first_color
            else:
                color = second_color
            print(color, end=' ' if y+1 < m else '')
        print()

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    solve(n, m, x1-1, y1-1, x2-1, y2-1)
