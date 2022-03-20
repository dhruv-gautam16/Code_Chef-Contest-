from typing import Counter

def getlist():
    return list(map(int, input().split(" ")))

def solve(t):
    n = str(input())
    ecount = 0
    ocount = 0
    for i in n:
        if int(i) % 2 == 0:
            ecount += 1
        else:
            ocount += 1
    if (ecount >= 2 and int(n[len(n) - 1]) % 2 == 0) or (ocount >= 2 and int(n[len(n) - 1]) % 2 != 0):
        print("YES")
    else:
        print("NO")
try:
    for i in range(int(input())):
        solve(i)
except:
    pass