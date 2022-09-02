t = int(input())
for i in range(t):
    n = int(input())
    o = 5
    e = 4
    odd = []
    even = []
    for i in range(n):
        odd.append(o)
        even.append(e)
        o += 2
        e += 2
    for i in odd:
        print(i , end = " ")
    print()
    for i in even:
        print(i , end = " ")
    print()