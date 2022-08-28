# cook your dish here
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    vals = list(map(int, input().split()))
    vals.sort()
    gaps = m-1
    cuts = 0
    while vals[0] < gaps:
        cuts += vals[0]
        gaps = gaps - (vals[0]+1)
        vals.pop(0)
        # print(vals)
    
    print(cuts+gaps)