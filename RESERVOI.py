# cook your dish here
def solution():
    h, w = map(int, input().split())

    R = [list('A'*(w+2)) for i in range(h+2)]
    R[-1] = list('B'*(w+2))

    for r in range(1, h+1):
        row = input();
        for c in range(1, w+1):
            R[r][c] = row[c-1]
    
    for r in range(1, h+1):
        for c in range(1, w+1):
            if R[r][c] == 'W':
                if R[r][c-1] == 'A' or R[r][c+1] == 'A' or R[r+1][c] == 'A':
                    print("no")
                    return
            if R[r][c] == 'B':
                if R[r+1][c] == 'A' or R[r+1][c] == 'W':
                    print("no")
                    return
    print("yes")

T = int(input())
while(T > 0):
    T = T - 1
    solution()