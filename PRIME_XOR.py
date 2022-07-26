# cook your dish here
from sys import stdin
for _ in range(int(stdin.readline())):
    x, y = map(int, stdin.readline().split())
    z = x^y 
    arr = [2]
    if x%2:
        arr.append(x^2)
    if y%2:
        arr.append(y^2)
    if z%2:
        arr.append(z^2)
    arr.sort()
    print(*arr)